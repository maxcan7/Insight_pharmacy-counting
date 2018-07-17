# Insight_pharmacy-counting
My Insight Data Engineering Fellowship pharmacy-counting code challenge repo

Instructions:
1. Open git bash and cd to the git repo
2. Enter the following code in bash(no quotes): "chmod +x pharmacy_counting.sh".
   This allows the shell script to be executed.
3. Type (no quotes): "./pharmacy_counting.sh" to run the shell script
4. The shell script calls to a python module pharmwrapper.py in the src folder, which
   runs the function pharmwrite in the module pharmacy_counting.py with the input 
   itcont.txt in the input folder, and outputs a file top_drug_cost.txt in the output
   folder. So long as the input is a .txt file in the same format as itcont.txt with the fields 
   drug_name and drug_cost, it will be flexible to different inputs. The output can be named anything.
   Because the input to pharmwrite includes the path, the paths can also be adjusted by adjusting the 
   fields in the pharmwrapper module.
5. To test the shell, follow the steps outlined below in Test Instructions.

Note that the python modules were written without the use of tools such as 
pandas or numpy.

Test Instructions:
1. Open git bash and cd to the git repo/test_suite
2. Enter the following code in bash(no quotes): "chmod +x run_tests.sh".
   This allows the shell script to be executed.
3. Type (no quotes): "./run_tests.sh" to run the shell script
4. Should output the results.txt in the test_suite folder and the test files into 
   the folder ./tests/test_1/

