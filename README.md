Third Practice Project: Data Cleaning with Pandas
This is my third attempt at data cleaning using Pandas, and yes, I still hadn’t learned matplotlib at this stage, so once again, I used colorama for visualization. 
This dataset is significantly larger than the ones used in the previous projects, meaning we’re dealing with a much higher volume of data this time.

Initial Impression

At first glance, this project may look very similar to the previous one, with just a few extra lines of code. So, what’s new here? 
Well, while it’s true that no groundbreaking techniques were added, repeating the same process with a completely new dataset serves as an excellent practice to test consistency.
It challenges you to see if you’ve mastered data cleaning with a standard approach.

Educational Highlight

Although this project builds on previous concepts, there’s an important learning point here that deserves special attention!
Using the replace() function, I modified row values to make them more meaningful and easier to understand for people who might not be familiar with the original dataset.
For example:
<=50 → More than 50K
This transformation makes the data more user-friendly and intuitive, especially for presentation purposes.

Output

The output remains similar to the previous projects:
1️⃣ The cleaned dataset is displayed first.
2️⃣ Then, using colorama, I answered a few key questions with color-coded outputs:

Green: Most common educational degree.

Light Blue: Most frequent marital status.

Blue: Most common gender.

Red: Most common skin color.

Pink: Country with the largest representation in the dataset.

Yellow: The highest income group.
