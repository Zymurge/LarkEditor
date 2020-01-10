# LarkEditor
A project spawned by a challenging interview question, to build a rules based validation engine.

## Why
Following a whiteboard interview session where I was challenged with this problem, I wasn't happy with the solution I hacked together. The problem stuck in my head, and in particular, the use of a Tree data structure to solve the problem. Having no recent past experience with Trees, I read up on them a bit and decided to put this solution together as part of my life long learning mission. Most of the work was done offline in the air while flying back and forth from SF to the Middle East during a recent family trip.

## What
The goal is to build a validation engine for a chatbot service script. It looks at a dialogue that alternates between chatbot questions and possible user responses. The hieracrchy is represented by prefixed tabs per line. It should be able to apply a series of dynamic rules to validate content and structure of both questions and answers. The original ask was to tag lines various colors based on whether they met or failed a particular validation for subsequent display in an HTML based editor. Given that I didn't remember all of the rules and colored responses, I built it with a generic tagging approach that marks up failed lines and for which rules they failed. In theory that would allow the rendering engine to make it's own decisions on how to display the results.

## Usage
- Construct a LarkEdit instance with the text data to be parsed into a Tree
- Call the Validation method with an array of rules to be applied, returning the marked up version of the text data
