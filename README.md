# CHASE-2018
In this repository you will find all the necessary steps to replicate the method available in the paper "Who Gets a Patch Accepted First? Comparing the Contributions of Employees and Volunteers", published at CHASE 2018. 

## Reproducing the dataset:
If you want to create your own version of the dataset execute the file "<i>script.py</i>" [[1]](https://github.com/fronchetti/CHASE-2018/blob/master/script.py) using Python 2.7. After the script execution, all the files will be saved in a folder called "Dataset", and you may need to allow this process in your system. We have already made available a ready copy of this folder in this repository [[2]](https://github.com/fronchetti/CHASE-2018/tree/master/Dataset).

Tips for dataset replication:
* In line 237, you can add more projects to be extracted (They need to be on GitHub).
* Between line 226 and 233 you can decide which of the dataset files you want to extract using the script. For example, if you just want the contributors of the projects use just the R.contributors() method and comment on the remaining lines. But pay attention, some files just can be extracted if others were already collected, so be careful.

### Dataset Structure:
⋅⋅* Dataset: <br>
⋅⋅*⋅⋅*⋅⋅* Project: <br>
⋅⋅*⋅⋅*⋅⋅*⋅⋅*⋅⋅* about.json (General information about the project) <br>
⋅⋅*⋅⋅*⋅⋅*⋅⋅*⋅⋅* contributors.json (All the contributors of the project) <br>
⋅⋅*⋅⋅*⋅⋅*⋅⋅*⋅⋅* externals.csv (All the externals contributors of the project) <br>
⋅⋅*⋅⋅*⋅⋅*⋅⋅*⋅⋅* pull_requests.json (All the pull requests of the project) <br>
⋅⋅*⋅⋅*⋅⋅*⋅⋅*⋅⋅* pull_requests_files.json (Files used in each merged/closed pull request) <br>
⋅⋅*⋅⋅*⋅⋅*⋅⋅*⋅⋅* unit_test_files.csv (Pull requests files that are probably related to unit tests) <br>
⋅⋅*⋅⋅*⋅⋅*⋅⋅*⋅⋅* merged_pull_requests_summary.csv (General information about each merged pull request) <br>
⋅⋅*⋅⋅*⋅⋅*⋅⋅*⋅⋅* closed_pull_requests_summary.csv (General information about each closed pull request) <br>

## Visualizing the charts:
With the dataset in hands, you can reproduce the charts using "<i>charts.R</i>" [[3]](https://github.com/fronchetti/CHASE-2018/blob/master/charts.R). The values defined in the lines of this script were manually written, based on the values that we found generating subsets for each project in the dataset. We created these subsets using conditionals that can be seen in "<i>script.R</i>" [[4]](https://github.com/fronchetti/CHASE-2018/blob/master/script.R). To find merged pull requests created by internals that attended to the best pratice three, for example, we created the conditional "<i>user_type == "Internals" & second_line_is_blank == "True"</i>", using data from the <i>merged_pull_requests_summary.csv</i> file of each project.

## Help?
Send us an e-mail:
fronchetti at usp . br
