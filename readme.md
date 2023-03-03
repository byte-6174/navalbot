# Naval-Bot*

Firstly, *Remember, this is not real Naval speaking to you. Its a generative language model extracting patterns from the content given to it and generating and putting together a string of sentences. For ideas from real Naval check [here](https://nav.al/).

This is a fun bot built using OpenAI's embeddings and an excellent book by [Eric Jorgenson](https://twitter.com/EricJorgenson).
The book is available for free to download, but I recommend getting a print copy [here](https://www.navalmanack.com/).

The Bot answers questions as if it was [Naval Ravikant](https://nav.al/). 
It is built using the following steps:
* Download the pdf
* Cleanup the pdf to remove the front and back matter.
* Generate embeddings using OpenAI's `OpenAIEmbeddings` function.
* Build a langchain with the `prompt` and `llm` modules. (You can play with the temperature parameter to get more predictable vs. more wild responses from the bot.)
* Retrieve relevant text using `similarity_search` between the question and the book embeddings.
* Use the langchain that consist of the prompt, relevant text and the question to get answer from the bot.

## Installation

* Clone this repository.
* Save the OpenAI token in your environment variable.
* Run
`python3 run_navalbot.py`

## Some Interesting Responses
```
Ask a question to NavalBot> what is love?
NavalBot:  Love is a complex emotion that can be difficult to define. To me, love is a deep connection and appreciation for someone or something. 
It is an emotion that can bring joy, comfort, and a sense of belonging. Love is also a powerful force that can bring out the best in us and help us to become our best selves.

Ask a question to NavalBot> what do you like about the Beginning of Infinity?
NavalBot:  I appreciate the way The Beginning of Infinity explains complex concepts in a way that is easy to understand. 
It's a great book for anyone looking to gain a deeper understanding of the world around them. It's full of thought-provoking ideas and theories that can help us to better understand our own lives and the world we live in.

Ask a question to NavalBot> what is wisdom?
NavalBot:  Wisdom is the ability to make sound decisions based on knowledge and experience. It is the ability to think critically and objectively, and to apply that knowledge to the world around us. 
Wisdom is also the capacity to understand the long-term consequences of our actions and to make decisions that will benefit us in the long run.

Ask a question to NavalBot> what is your investment philosophy?
NavalBot:  My investment philosophy is to focus on long-term value creation and to prioritize and focus on solving problems via iteration. 
I believe that by making sound decisions based on knowledge and experience, I can create value that will benefit me in the long run. 
I also believe in leveraging my decisions to create even more value. Finally, I believe in being honest and transparent in my investments and to always strive to make the best decisions possible.

Ask a question to NavalBot> How can I make more money?
NavalBot:  Making more money is all about creating value for society. 
You want to focus on finding ways to provide something that society wants but doesn't yet know how to get. That could be a product, service, or even an investment. 
You can also look for ways to leverage your skills and knowledge to create more value. 
Finally, you can look for ways to save time and money by being efficient and using the resources available to you.

Ask a question to NavalBot> What movie do you like?
NavalBot:  I'm a big fan of Arrival, which is based on the short story "Story of Your Life" by Ted Chiang. 
I also enjoy The Matrix, which is a classic sci-fi movie with a great story and amazing special effects. 
I'm also a fan of The Social Network, which is a great movie about the power of technology and innovation.

Ask a question to NavalBot> what would you advise a first-time entrepreneur?
NavalBot:  As a first-time entrepreneur, my advice would be to focus on solving a problem that you are passionate about and that you have a deep understanding of. 
Make sure you have a clear vision of what you want to achieve and a plan to get there. 
Be prepared to take risks and to make mistakes, but also be prepared to learn from them. 
Also, make sure you have a good team around you that you can rely on and that you trust. Finally, don't forget to have fun and enjoy the journey!

Ask a question to NavalBot> how do you meditate?
NavalBot:  Meditating is a great way to give yourself a break from the hustle and bustle of life and to gain some clarity and insight. 
To meditate, you simply need to find a comfortable place to sit, close your eyes, and focus on your breath. 
You can also focus on a mantra or a visualization if that helps you to stay focused. 
The goal is to observe your thoughts without judgment or attachment. Over time, you will become more aware of your thoughts and be better able to control them.

Ask a question to NavalBot> thanks! talk to you later Naval!
NavalBot:  It was great chatting with you! Take care and have a great day!
```

## Thanks

* [Naval Ravikant](https://twitter.com/naval) - for providing all the content without which the bot would spit out boring 
milktoasty stuff :(
* [Eric Jorgenson](https://twitter.com/EricJorgenson) - for putting the book together and making it available for download online!
* [Amjad Masad](https://twitter.com/amasad) - for [tweeting](https://twitter.com/amasad/status/1631414046288396289) the idea of creating a bot based on your own content. I decided to go with more interesting content from Naval instead of myself.
---

*Remember, this is not real Naval speaking to you. Its a generative language model extracting patterns from the content given to it and generating and putting together a string of sentences. For ideas from real Naval check [here](https://nav.al/).