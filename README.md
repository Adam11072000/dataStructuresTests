# dataStructuresTests
Welcome Students!

generate_tests and generate_outputs are created by me, the test runner run_tests.py is not made by me!

steps to run tests:
  1) download directory into your main directory on your local computer/sharat.
  2) make sure the variable MY_EXEC is the path to your exec file.
  3) run this command on th sharat: python3 run_tests.py
  4) if all is okay then valgrind and diff is okay.



if you want to create more tests, change generate_tests file and only this file!
chnage variable NUM_OF_TESTS and generate output using this command in bash:

for i in{1..NUM_OF_TESTS}
do
python3 generate_output.py ./input/$i.txt ./expected/$i.txt
done


