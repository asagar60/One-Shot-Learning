# One Shot Learning

Overview
---
We will implement One shot learning to build a model which will correctly make predictions given only a single example of each new class.


Dataset
---
I have used omniglot dataset by Brenden Lake.
It contains 1623 different handwritten characters from 50 different alphabets. Each of the 1623 characters was drawn online via Amazon's Mechanical Turk by 20 different people.

How to Train the model ?
---
1. Clone this repo
2. Download omniglot dataset from here. https://github.com/brendenlake/omniglot.

    For this implementation we need only 'images_background.zip' and 'images_evaluation.zip' .
3. Extract the folder
4. ```bash
python load_data.py
```
5. Execute ipython notebook cells from `One_shot_implementation.ipynb`.

Download pre-trained weights from [here](https://drive.google.com/file/d/1JmP0TnsotXA6CNDIE0-6MpkBun7KKS2s/view?usp=sharing).
