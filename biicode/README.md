Biicode C/C++ dependency manager
=================================
New with biicode? Check the [getting started guide](http://docs.biicode.com/c++/gettingstarted.html).

How build it?
------------------
Building it is too easy:

    $ git clone git@github.com:google/flatbuffers.git
    $ cd flatbuffers
    $ bii buzz

It creates all the necessary structure to build flatbuffers with biicode build system and try some selected examples.

By default, the first use applies all the changes to the repository, if you want to revert these ones, set the `BII_FLAT_REVERT_CHANGES` environment variable to `True` and run `bii work` to keep your original code and undo the biicode changes.

    $ export BII_flatbuffers_REVERT_CHANGES='True' # for Windows users: set BII_flatbuffers_REVERT_CHANGES=True
    $ bii work


How use it in other projects?
----------------------------------
Create new biicode project and create an empty block:
    
    > bii init myproject
    > bii new myuser/myblock

Include the header you need from this block into your source code, for example:

    #include "fenix/flatbuffers/Net/include/flatbuffers/Net/HTTPServerRequestImpl.h"
    #include "fenix/flatbuffers/Foundation/include/flatbuffers/Foundation.h"

Open **biicode.conf** file and write a *[requirements]* section to this block:

    [requirements]
        # This file contains your block external dependencies references
        fenix/flatbuffers(develop): 0

You could also keep your `#include`'s like `"flatbuffers/Foundation.h"` and `"flatbuffers/Net/HTTPServerRequestImpl.h"` adding the include mapping configuration into the mentioned file:

    [includes]
        flatbuffers/Net/*.h: fenix/flatbuffers/Net/include
        flatbuffers/*.h: fenix/flatbuffers/Foundation/include

Program your code and build it: 

    > bii cpp:build # This command will build your project and the flatbuffers dependencies

You can check [the examples/flatbuffers(develop) block](https://www.biicode.com/examples/examples/flatbuffers/develop) with some examples using *flatbuffers C++ develop version* with biicode.
