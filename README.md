# Chronological Audio Bible Rename

Take audio files that are already in standard order, with each chapter as a separate mp3 file, and rename them to be in the desired chronological order.

## Overview

### Two scripts

1. The first script generates the list of audio files in a folder.
    ```
    bible-mp3-generate-list.py
    ```

2. The second script uses the generated list to rename the audio files.
    ```
    bible-books-rename.py
    ```

## Usage

1. Edit the `bible-mp3-generate-list.py` file, and change the folder location to where your audio files are saved.
    ```python
    os.chdir('/home/user/bible/')
    ```

2. Run the script to output the list.
    ```console
    python3 bible-mp3-generated-list.py
    ```

3. Copy/paste the list into a temp file and *manually* re-order the list so it's in the desired chronological order. An example is [here](https://whitefieldsprayer.blogspot.com/2012/10/every-chapter-of-entire-bible-in.html).

4. Replace the `chapters` list at the top of the `bible-books-rename.py` file with your new chronological list.
    ```python
    chapters = [
      ["01 Genesis","01"],
      ["01 Genesis","02"],
      ["01 Genesis","03"]
      etc...
    ```

5. Edit the `bible-books-rename.py` file, and change the folder location.
    ```python
    os.chdir('/home/user/bible/')
    ```

6. Comment out the following line to only see a preview of what will be renamed.
    ```python
    # os.rename(file, file_renamed)
    ```

7. Run the script to see a preview. Un-comment the line above and re-run the script to rename the files.
    ```console
    python3 bible-books.rename.py
    ```
