redis_mock_data_generator
======
{Syntax and interpreter ver. 3}

Overview
------
Implementation of the mock data generator for Redis (key–value store).

Goals
------
Because It's a dull thing to hammer test data into a freshly installed Radish with your hands, this script was written. Long live automation!

Usage
------
After running the script: 

    $ python3 redis_mock_data_generator.py

A text file will be created at the root of the directory ***'redis_mock_data_file.txt'***.
The file will contain random datasets, based on the standard (built-in) Redis (string, list, set, zset, hash) data types, for streaming key-value storage filling.

To fill the storage with data, use the following construction:

+ linux    

    $ cat redis_mock_data_file.txt | redis-cli --pipe

+ windows  

    $ type redis_mock_data_file.txt | redis-cli --pipe

p.s. All string values in the data are replaced by their hashes (implemented using the function ***'hashlib.sha512()'*** standard python library).

License
------
This software is free to use under the **MIT** license.

