"""Madlibs Stories."""

from flask import Flask, request
from stories import Story

app = Flask(__name__)


@app.route("/")
def home():
    prompts = story.prompts
    return render_template("home.html", prompts=prompts)


@app.route("/story")
def madlibs_story():
    answers = {}
    for prompt in story.prompts:
        answer = request.args.get(prompt)
        answers[prompt] = answer
    text = story.generate(answers)
    return render_template("story.html", text=text)


class Story:
    """Madlibs story.

    To  make a story, pass a list of prompts, and the text
    of the template.

        >>> s = Story(["noun", "verb"],
        ...     "I love to {verb} a good {noun}.")

    To generate text from a story, pass in a dictionary-like thing
    of {prompt: answer, promp:answer):

        >>> ans = {"verb": "eat", "noun": "mango"}
        >>> s.generate(ans)
        'I love to eat a good mango.'
    """

    def __init__(self, words, text):
        """Create story with words and template text."""

        self.prompts = words
        self.template = text

    def generate(self, answers):
        """Substitute answers into text."""

        text = self.template

        for (key, val) in answers.items():
            text = text.replace("{" + key + "}", val)

        return text


# Here's a story to get you started


story = Story(
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """Once upon a time in a long-ago {place}, there lived a
       large {adjective} {noun}. It loved to {verb} {plural_noun}."""
)
