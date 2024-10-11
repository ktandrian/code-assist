# Demo 4

Generating scripts to aggregate data.

## Prompt

1. Open `input.csv` file.

2. Enter this prompt:
   ```
   buatin script python untuk membaca file input.csv, kemudian hasilkan output ke output.csv yang isinya nama company dan jumlah karyawannya.
   ```

3. If the script uses pandas, enter this prompt:
   ```
   Jangan pake pandas dong.
   ```

4. Save the file as `main.py` in `demo-4` folder.

5. Run the script.
   ```bash
   python main.py
   ```

6. Check the `output.csv` file. The result should look like this:
   ```csv
   Company,Employee Count
   Google,165
   Apple,165
   Meta,165
   Amazon,16
   ```

##

2024 &copy; Ken Tandrian