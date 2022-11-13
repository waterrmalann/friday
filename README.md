# F.R.I.D.A.Y | Desktop Virtual Assistant

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)   ![Windows](https://img.shields.io/badge/Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white)   ![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)

---

An extremely versatile, modular, and sophisticated desktop virtual assistant written in pure Python. Uses a plugin architecture where pretty much every part of the assistant is an individual component that can be written in any way as long as it plugs into the core assistant. The name originates from the term "man/girl Friday", meaning go-to person and is heavily inspired by the [replacement virtual assistant](https://marvelcinematicuniverse.fandom.com/wiki/F.R.I.D.A.Y.) created by Tony Stark (Iron Man).

The primary response engine of Friday, SBRE implements python programs written in a specific format (inheriting from a Skill class) as "Skills" that it can perform based on command triggers from the user. A skill may be something as simple as telling the assistant to flip a coin to something complex as a password manager or an AI image enhancer. There are a few skills already defined:

| Skill | Description | Example |
| --- | --- | --- |
| Coin Toss | Toss a coin and get the outcome. | "Flip a coin" |
| Dice Roll | Roll a dice and get the outcome. | "Roll a dice" |
| Date/Time | Get information about date/time. | "What's the time?" |
| 8ball | Get replies from the magic 8ball. | "Ask 8ball if today will be a good day." |

**See the [Wiki](https://github.com/waterrmalann/friday/wiki) for more information about how FRIDAY handles and processes commands.**

![Screenshot](https://github.com/waterrmalann/friday/blob/main/documentation/desktop_demo.jpg)

*A dumb version of FRIDAY (4 skills and no chat engine) running in the Windows terminal.*

---

### 🚀 Setup

Setting up Friday is quite simple, follow the instructions below:

1. [Clone the repository](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository-from-github/cloning-a-repository).

```sh
git clone https://github.com/waterrmalann/friday.git
```

2. Install the dependencies.

```sh
python -m pip install -r requirements.txt
```

3. Run the assistant within the terminal.

```sh
python "driver_console.py"
```

---

### 🤝 Contribution

Contributions are welcome and greatly appreciated! Feel free to open a pull request to fix any issues or to make improvements you think that should be made.
- **Contributions to the core.**
  - I believe the core is pretty stable as is but it could definitely be improved in many ways. You could fix anything that bugs you or even rewrite major parts of the assistant as long as they are an improvement in some way (performance, readability, consistency, etc..) and not a downgrade. If you're in doubt about whether the PR would be accepted or not, you can always open an issue to get my opinion on it.
- **Contributions to the response engines.**
    - You can choose to improve, or add more commands for the Simpleton Response Engine (SRE) or create skill files for the Skill Based Response Engine (SBRE) that inherits from the Skill class. 

License
----

This project is licensed under the **AGPLv3 License**, see [LICENSE](LICENSE).
