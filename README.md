# LexiT: Vocabulary Training App

LexiT is a terminal-based vocabulary training application designed primarily for Linux users, though it is also compatible with Windows and Mac systems through terminal tools. The name "LexiT" cleverly combines "lexicon," referring to the vocabulary of a language, with "terminal," emphasizing its command-line interface.

## Key Features

- **Score Tracking:** LexiT tracks your performance, allowing you to monitor your progress as you practice.
- **Adaptive Learning:** The app prioritizes words that you've struggled with by asking them more frequently. This helps reinforce your memory and improve retention.
- **Randomized Questions:** To keep the learning experience engaging, LexiT presents vocabulary questions in a random order, ensuring a varied practice each time you use it.
- **Cross-Platform Compatibility:** While primarily developed for Linux, LexiT can be run on Windows and Mac, making it accessible to a broader audience.
- **Example Database:** LexiT includes an example database derived from the *Passt schon 4* German workbook, providing a clear guideline on how vocabulary words should be structured and added to the application.

## Instalation

1. Clone the repository:
    ```bash
    git clone <repository-url>
    cd LexiT
    ```

2. Ensure you have Python installed. You can check this by running:
    ```bash
    python --version
    ```

## Running the Application

To run the application, use the following command:

```bash
python run.py <vocab.json> [<lesson_id> [<page_id>]]
```

**Parameters**
- **<vocab.json>:** The path to the vocabulary database file (must be in JSON format).
- **<lesson_id> (optional):** The specific lesson you want to quiz on (e.g., L1, L2, etc.).
- **<page_id> (optional):** The specific page within the lesson to quiz on (e.g., 1, 2, etc.).

**Examples**
- To run the quiz for all vocabulary in lesson L1:
```bash
python run.py vocab.json L1
```

- To run the quiz for a specific page in lesson L3:
```bash
python run.py vocab.json L3 2
```

- To run the quiz for all vocabulary without specifying a lesson or page:
```bash
python run.py vocab.json
```


