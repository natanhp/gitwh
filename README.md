# gitwh

Github Webhook Engine Helper

## Usage

1. Create and initialize repositories folder, to collect all of your repositories
    ```bash
    $ mkdir repositories/
    $ cd repositories/
    $ gitwh init here
    ```
    or
    ```bash
    $ gitwh init repositories/
    ```
2. Add Repository
    ```bash
    $ gitwh add https://github.com/user/repository1.git
    ---- Repository Form ----
    Webhook Header Secret (default: null): rep1secretkeyabcdefg
    Listen Endpoint (default: /user/repository1): /repository1/webhook
    Status File Descriptor Name (default: user_repository1.status): rep1.status
    Log File Name (default: user_repository1.log): rep1.log

    ---- Confirmation ----
    Secret              : rep1secretkeyabcdefg
    Endpoint            : /repository1/webhook
    Status Descriptor   : rep1.status
    Log File            : rep1.log
    Deployment Script   : build.sh

    Is this correct (yes/no) ? yes

    Repository Created !

    $ gitwh list
    Registered repositories
    ID          URL
    ---         ---
    1           https://github.com/user/repository1.git
    ```

3. Run gitwh
    ```bash
    $ gitwh run
    host and port is not set using fallback...
        | Using Host 0.0.0.0
        | Using Port 5656
        ... OK!
    Running gitwh webhook listener... OK!
    fetching triggered when POST request received by:
        1. http://localhost:5656/repository1/webhook
    ```
    or, set your own host and port
    ```bash
    $ gitwh run --host=0.0.0.0 --port=6000
    ```