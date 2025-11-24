# Timed Math Challenge

This document outlines the core components and goals of the Python script designed for testing mental arithmetic skills.

## Problem Statement

Let's face it: mental math skills get rusty. The problem we set out to solve was the lack of a quick, no-fuss way to get better at basic arithmetic under pressure. The core need is to randomize problems, accurately time the user's performance, track the score, and provide a detailed post challenge review so anyone could actually learn from the mistakes they made when the clock was running.

## Scope of the Project

The scope of this project is limited to a single-user, console-based application implemented purely in standard Python 3.x.

### The script's responsibility is confined to the following:

___Generation___: Creating simple, two-operand arithmetic problems (+, -, *).<br>
___Interaction___: Accepting numerical input from the user via the console.<br>
___Measurement___: Calculating the total duration taken to answer a fixed set of questions.<br>
___Reporting___: Displaying the final score, time, and offering a line-by-line review of the results.<br>

### Out of Scope:

* Graphical User Interfaces (GUIs).<br>
* Complex operations (e.g., division, exponents, parenthesis).<br>
* Multiplayer or network features.<br>

## Target Users

The primary target users are individuals seeking to improve their foundational math skills:

__Grade School students__: Users who are mastering basic arithmetic facts and need consistent, timed repetition.<br>
__Adult Learners__: Individuals refreshing core math skills for exams, career changes, or general cognitive exercise.<br>
__Educators__: People who need a quick, no-setup tool to quiz students or children.<br>

## High-Level Features

The application is built around four core feature groups:

### Challenge Setup:
* Allow configuration of the number of questions (defaulting to 10).<br>
* Random generation of numbers (1-20) and operators (+, -, *).<br>

### Timing & Scoring:
* See the time taken to complete the challenge
* Track the number of correct answers.

### User Interaction & Robustness:
* Present questions clearly in sequence.
* Handle non-numeric input gracefully (via try-except).

### Reporting & Review:
* Calculate and display the total time and final score percentage.
* Provide a detailed optional review section showing the problem, user's answer, and the correct answer for every question.
