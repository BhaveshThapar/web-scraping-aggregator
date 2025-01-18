import subprocess

def save_output(script_name, output_file):
    try:
        result = subprocess.run(
            ["python", script_name],
            capture_output=True,
            text=True,
            check=True
        )
        with open(output_file, "a") as file:
            file.write(f"Output from {script_name}:\n")
            file.write(result.stdout)
            file.write("\n" + "=" * 50 + "\n")
        print(f"Output from {script_name} saved to {output_file}.")
    except subprocess.CalledProcessError as e:
        print(f"Error running {script_name}: {e}")

if __name__ == "__main__":
    output_file = "output.txt"

    with open(output_file, "w") as file:
        file.write("Output:\n" + "=" * 50 + "\n")

    scripts = ["star_wine.py", "yelp_scraping.py"]
    for script in scripts:
        save_output(script, output_file)
