## Assignment - 1: Bash Scripting
#### Software Systems Development

###### Answer 1
1.a ) `mkdir` is used for creating directory and `cd` for changing directory. `&&` is used for combining both command into one line.
1.b ) `touch` is used for creating files. `lab{1..5}.txt` will create lab1.txt, lab2.txt, lab3.txt, lab4.txt and lab5.txt in one go.
1.c ) `xargs` reads items from standard input as separated by blanks and executes a command once for each argument. `mv` command is used for renaming file.
1.d ) `ls` is used for listing files. `-lhSr` stands for long-listing format, human-readable, sort and reverse.
1.e ) `find ~ -maxdepth` is used for finding files at given max-depth from the root folder.
1.f ) `find . -name` is used for finding the given file name from the current dierctory(Assignment-1).

###### Answer 2
Using `compgen -c`, all possible command keywords are stored into the variable. Instead of finding all the permuatation of the input word and comparing it with all possible command keywords, both input and command word are sorted (lexographical sorting) and then compared only once.
To make it more efficient, comparison is only done when the length of input word and command word are same.

###### Answer 3
`history` command is used for getting all the history of commands run on terminal/shell. 
The current history for your current shell is stored in memory, it is only written to the HISTFILE (~/.bash_history) once the shell is exited.
Used `~/.bash_history` file, and then took last 10 (latest) commands, sorted it, took the unique count using `uniq -c`, again reverse sorted based on number using `sort -rn`, and then output top 10 values using `head` command. 
`awk` is also used to fetch the first field (command name) from the complete command.

###### Answer 4
Using `tr` command, all brackets and extra spaces between two numbers(any data) are removed.
`sed` command is then used to remove leading and trailing spaces, if it exists. Finally `(` and `)` brackets are appended at start and end, respectively.

###### Answer 5
Initially the input word is converted to lowercase using `${string,,}`. To reverse the input word, `rev` command is used. If both input and its reversed format gets matched, `Yes` is printed, else `No`.

###### Answer 6
`$@` is used to get all parameters passed into the script. It takes each parameter as a separate quoted string.  `a**b` represent a^b.

###### Answer 7
`ps -au` is used to show all running processes for all users, with details like `USER, PID, %CPU, %MEM, Status, TIME`.
To get all `PID's` (2nd field), I used the `tr` command. Finally to remove the first word `'PID'` from the list, I took the length (`len`) of list using `wc -l`, and then took bottom `len-1` entries from list using `tail` command and stored it into 'pid.txt'.
Finally top `n` commands were echoed using `head -n` command.

###### Answer 8
`crontab` command is used to run 'crontab_file'. To check if 'crontab_file' is properly formatted, I ran that file and checked the exit status. If the `exit status` is equal to `0`, then command executed successfully (meaning formatting was proper), else any value other than `0`, indicates error (meaning improper formatting of 'crontab_file')
To avoid printing error, in-case of improper formatting of 'crontab_file', `>> /dev/null 2>&1` is used which redirects standard output `(stdout)` to `/dev/null`, which discards it. `2>&1` redirects `standard error (2)` to `standard output (1)`, which then discards it as well since standard output has already been redirected.

###### Answer 9
First all spaces are removed using `sed 's/ //g'`. Then length (`l`) of the remaining input word is calculated. If the `l<=1`, then `Invalid` is output and I exit. Else, in a loop from the `l-1` to `0`, I followed `The Luhn Algorithm`, and checked if final sum of all digits, is divisible by `10` or not, and gave output accordingly.

###### Answer 10
For calculation purpose, I have used `bc` command, because we can't do floating-point arithmetic natively in Bash. `bc` can be considered as mathematical scripting language. `case` is used in the code for performing seperate calculations for seperate operator. Finally `printf "%.4f" $result` is used to print 4-precision for decimal number result on standard output.