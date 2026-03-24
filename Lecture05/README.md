# Lecture 06: Introduction to RDKit

RDKit is a powerful open-source cheminformatics toolkit designed to simplify chemical data processing. Importantly, it has specialized classes to deal with molecular structures, allowing us to easily represent, modify, and visualize molecules. RDKit is a useful tool both in research and in industry (and some of your TA's proudly consider themselves RDKit hackers :sunglasses:)

Today we will go through some of RDKit's most useful functionalities:
1. **Reading, writing, and visualizing molecular data**
2. **Calculating descriptors**
3. **Representing molecules with "fingerprints".** 


## Setup

Get your exercises by running `git pull` from your `practical-programming-in-chemistry-exercises` folder. Copy `Lecture06` to your `ppchem` folder (or whatever folder you're using to complete your exercises), and complete the exercises from there. 

This week, we need one extra package: `py3Dmol`. Install it with `pip` into your `ppchem` environment. Update the `.env` file just like you did yesterday. Try to see what you remember from yesterday, but if you need help, walk through the instructions in Lecture05 with `py3Dmol` instead of `matplotlib`. 

<details>
<summary>Solution: Commands</summary>

Don't forget to repalce `path/to/ppchem` with your path!

```bash
cd <path/to/ppchem>
conda activate ppchem
pip install py3Dmol
conda env export > env.yml
git add env.yml
git commit -m "Add environment file"
git push origin main
```

</details>




## Exercise

Now you're ready to give the [exercises](06_exercise.ipynb) a go!
