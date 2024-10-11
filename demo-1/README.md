# Demo 1

Let's create a weather app from scratch using OpenWeather API.

## Getting Started

1. Open the terminal.
2. Make sure you are in `demo-1` folder. If not, run `cd demo-1`.
3. Create virtual environment by running `python -m venv .venv`.
4. Activate the virtual environment by running `source .venv/bin/activate`.

## Demo Guide

1. Go to the chat tab and enter this prompt:
   ```
   Hey, coba buatkan aplikasi Flask yang terhubung ke OpenWeather API untuk mendapatkan cuaca. Di halaman aplikasinya pengguna bakal bisa memasukkan nama tempat
   ```

2. On the top-right corner of the generated Python code, click "Open in a file" and save it as "app.py".

3. Gemini should provide you with `API_KEY` variable. Replace the content with your API key.
   ```
   API_KEY = "YOUR_API_KEY"
   ```

4. If Gemini also generates the HTML code, usually it will ask you to save it as "template/index.html". Let's deliberately save it as "index.html".

5. If no HTML code is generated, enter this prompt:
   ```
   Yaelah, buatin index.html juga dong!
   ```
   and save it as "index.html".

6. Generate the dependencies list by giving this prompt:
   ```
   Buatkan requirements.txt dong!
   ```

7. Run these command (these steps should be part of the first response):
   ```bash
   # Install dependencies
   pip install -r requirements.txt

   # Run the app
   python app.py
   ```

8. Open browser and access [http://127.0.0.1:5000/](http://127.0.0.1:5000).

9. You should expect an error message like this:
   ```
   jinja2.exceptions.TemplateNotFound: index.html
   ```

10. Pass this prompt to Gemini:
    ```
    Ah parah, error nih! Errornya jinja2.exceptions.TemplateNotFound: index.html
    ```

11. Follow the instructions to fix the app. Gemini should ask you to move the `index.html` file to the `templates` folder and restart the app.

12. Enter any city in the input box and see the result (e.g., Medan, Jakarta, Jambi).

13. Let's ask Gemini to redesign the UI using Bootstrap. Block the whole `index.html` file and enter this prompt:
    ```
    hmm tampilannya agak kurang ya, coba bantu ganti pake tailwind deh!
    ```

13. This time, open `index.html`, remove the content, and click "Insert in current file" button on the top-right corner of the generated HTML code.

14. (Optional) Check if the UI elements are good. In my case, the picture size is somehow too large, so I asked Gemini:
    ```
    fotonya kebesaran nih, kecilin dong
    ```

##

2024 &copy; Ken Tandrian
