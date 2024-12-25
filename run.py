import click
import os
import importlib.util
import time
from collections import namedtuple
from colorama import Fore, Style, init as colorama_init

colorama_init(autoreset=True)

Solution = namedtuple(
    "Solution", ['meta', 'input', 'parse_fn', 'a_fn', 'b_fn'])

@click.group()
def cli():
    pass


solutions = {}

def load():
    years = os.listdir("years")
    for year in years:
        solutions[year] = {}
        days = sorted([x for x in os.listdir(
            f"years/{year}") if x.endswith(".py")])

        for day in days:
            stripped_day = day[:-3]
            spec = importlib.util.spec_from_file_location(
                stripped_day, f"years/{year}/{day}")

            assert spec is not None
            assert spec.loader is not None

            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)

            if not hasattr(module, "meta"):
                raise Exception(f"Solution ({year}/{day}) is missing metadata")

            meta = module.meta()

            if not hasattr(module, "parse"):
                raise Exception(
                    f"Solution ({year}/{day}) is missing its parsing function")

            parse_fn = module.parse
            a_fn, b_fn = module.a if hasattr(
                module, "a") else None, module.b if hasattr(module, "b") else None

            if not os.path.exists(f"input/{year}/{stripped_day}"):
                raise Exception(f"Solution ({year}/{day}) is missing an input")

            with open(f"input/{year}/{stripped_day}") as f:
                input = f.read().rstrip()

            solutions[year][str(int(stripped_day))] = Solution(
                meta, input, parse_fn, a_fn, b_fn)

def measure(fn, *args):
    before = time.perf_counter_ns()
    res = fn(*args)
    return res, (time.perf_counter_ns() - before) / 1_000_000

@click.command()
@click.option("--year", type=str, required=False, help="Specify the year.")
@click.option("--day", type=str, required=False, help="Specify the day.")
@click.option("--clear", '-c', is_flag=True, help="Clears the screen.")
def run(year, day, clear):
    if clear:
        os.system("clear")

    if day and not year:
        click.echo(
            f"{Fore.RED}Error: You must specify a year if specifying a day.{Fore.RESET}")
        return

    if year and year not in solutions:
        click.echo(f"{Fore.RED}Error: Year {year} not found.{Fore.RESET}")
        return

    selected_years = [year] if year else solutions.keys()
    total_stars = 0

    for y in selected_years:
        days = solutions[y].keys() if not day else [day]

        for d in days:
            if d not in solutions[y]:
                click.echo(
                    f"{Fore.RED}Error: Day {d} not found in year {y}.{Fore.RESET}")
                continue

            sol = solutions[y][d]
            print(f"{Fore.GREEN}{y} Day {d}{Fore.RESET}{Style.DIM}")

            parsed, _ = measure(sol.parse_fn, sol.input)
            a, _ = measure(sol.a_fn, parsed)
            b, _ = measure(sol.b_fn, parsed)

            a_check = "solutions" in sol.meta and "a" in sol.meta["solutions"] and str(
                a) == str(sol.meta["solutions"]["a"])
            b_check = "solutions" in sol.meta and "b" in sol.meta["solutions"] and str(
                b) == str(sol.meta["solutions"]["b"])

            if a_check:
                total_stars += 1
            if b_check:
                total_stars += 1
            print(

                f"  {Style.DIM}Part 1: {Style.RESET_ALL}{a} {'⭐' if a_check else '❌'}")
            print(
                f"  {Style.DIM}Part 2: {Style.RESET_ALL}{b} {'⭐' if b_check else '❌'}")
            if not year or not day:
                print()

    if not year or not day:
        print(f"{Fore.YELLOW}Overall Stars: {Style.RESET_ALL}{total_stars} ⭐")

@click.command()
@click.option("--year", type=str, required=False, help="Specify the year.")
@click.option("--day", type=str, required=False, help="Specify the day.")
@click.option("--clear", '-c', is_flag=True, help="Clears the screen.")
def bench(year, day, clear):
    if clear:
        os.system("clear")

    if day and not year:
        click.echo(
            f"{Fore.RED}Error: You must specify a year if specifying a day.{Fore.RESET}")
        return

    if year and year not in solutions:
        click.echo(f"{Fore.RED}Error: Year {year} not found.{Fore.RESET}")
        return

    selected_years = [year] if year else solutions.keys()
    total_time, total_stars = 0, 0

    for y in selected_years:
        days = solutions[y].keys() if not day else [day]

        for d in days:
            if d not in solutions[y]:
                click.echo(
                    f"{Fore.RED}Error: Day {d} not found in year {y}.{Fore.RESET}")
                continue

            sol = solutions[y][d]
            print(f"{Fore.GREEN}{y} Day {d}{Fore.RESET}{Style.DIM}")

            parsed, parse_time = measure(sol.parse_fn, sol.input)
            a, a_time = measure(
                sol.a_fn, parsed) if sol.a_fn is not None else (None, 0)
            b, b_time = measure(
                sol.b_fn, parsed) if sol.b_fn is not None else (None, 0)

            a_check = "solutions" in sol.meta and "a" in sol.meta["solutions"] and str(
                a) == str(sol.meta["solutions"]["a"])
            b_check = "solutions" in sol.meta and "b" in sol.meta["solutions"] and str(
                b) == str(sol.meta["solutions"]["b"])

            total_day_time = parse_time + a_time + b_time
            total_time += total_day_time

            if a_check:
                total_stars += 1
            if b_check:
                total_stars += 1

            print(f"  {Style.DIM}Parse: {Style.RESET_ALL}{parse_time:.2f} ms")
            print(f"  {Style.DIM}Part 1: {Style.RESET_ALL}{a} {Style.DIM}({Style.RESET_ALL}{a_time:.2f} ms{Style.DIM}){Style.RESET_ALL} {'⭐' if a_check else '❌'}")
            print(f"  {Style.DIM}Part 2: {Style.RESET_ALL}{b} {Style.DIM}({Style.RESET_ALL}{b_time:.2f} ms{Style.DIM}){Style.RESET_ALL} {'⭐' if b_check else '❌'}")
            print(
                f"  {Fore.CYAN}Total: {Style.RESET_ALL}{total_day_time:.2f} ms{Fore.RESET}")
            if not year or not day:
                print()

    if not year or not day:
        print(f"{Fore.YELLOW}Overall Total: {Style.RESET_ALL}{total_time:.2f} ms")
        print(f"{Fore.YELLOW}Overall Stars: {Style.RESET_ALL}{total_stars} ⭐")


cli.add_command(run)
cli.add_command(bench)

if __name__ == "__main__":
    load()
    cli()
