bsvbip32
============

BIP32 Hierarchical Deterministic wallet functions - extends bitsv

Noticeboard
-----------

This project is still in alpha. Expect lots to change - pin your versions if you are using this code!

I will post a road map here in due course.

- I essentially want to have the "leaves of the BIP32 tree" inheriting all of the functionality of a bitsv.PrivateKey to make building prototype applications in Python a breeze.

Examples
---------

1. Create master node.

.. code-block:: python

    >>> from bsvbip32 import Bip32
    >>> xprv = Bip32("xprv9s21ZrQH143K4Un4SHjdvXpzzdQjpm7vVhQ79BMi5V58nptUo4NGqytwH68XAVj5LkDxjSqdVjdDinFCT8WqfBT7zigdtaGcrffTmBdwFH5")


2. Get receiving address for given derivation path (defaults to Electrum SV / Handcash path)

.. code-block:: python

    >>> # Get receiving addresses
    >>> xprv.get_child_addresses(derivation_path='0', index_start=0, index_end=5)
    ['1PPro3nLxMB7A1BJXfZkRDHCRugj8z4d7R',
     '169YSZGMvtHvKbRHTpYCQZWx1phfJp2DCe',
     '1PhGu2V5T5g26bHi6qKg2KmxpUQLuNwyKT',
     '16WGTyMx578ghUzKbuvSsg2BnRAorm7bhm',
     '168A5g1AeLvkRHekEDRKXzDDqHPLkr2yHD']

    >>> # Change addresses
    >>> xprv.get_child_addresses(derivation_path='1', index_start=0, index_end=5)
    ['1FUT1Yn7RcsXADpkfweiVrfkPurkFBDfuU',
     '1M126MVQst5XGGqV6gVuXxCAwTGkwwgspk',
     '1BX2BzUhuWCod14BMLYUFyMiXX2qhJbNX5',
     '1KyeAK4q2sc6bcZ9nem878oFcNo59dmr1c',
     '1EEAjPDQwoBzQmXoy89BZKX4wyGpELQTc5']

3. Master nodes (generated with an extended **private key** can generate child private keys).

.. code-block:: python

    >>> xprv.get_child_private_keys(derivation_path='0', index_start=0, index_end=5)
    [private_for <xpub6AJDyEAwA8V7aVsF4dU3Kfdp9dH7W85F8iaWqgXqoeXEGWKBP3e7PeW2s76FM4krswNPkuHHUxaDPLD8aYG3CGyYU539MpHUsWCXk2W4pfV>,
     private_for <xpub6AJDyEAwA8V7ec7QFow54ssKpgtys6JY2gUzmpKQnDGvs6UoqYbpuu1a9JYxWJZ4UkWoZLAsRF2w8QA2pxDpMjyuzHDmYMTB7mpuPk5bpM5>,
     private_for <xpub6AJDyEAwA8V7ho8mZJyWFcz9kWzb8QcCSizGLsHgjKZj4eFT9LeuhUFyRXNzCzZJCPfmR2fXG9VXhHKVWJa9ZPUWK89rmjdkhTbQDUTTLfA>,
     private_for <xpub6AJDyEAwA8V7kRxmXXwCp6v49KAHxdcpXpQe7YZn6YuNrte4CxbeN8aYm7F3EZQgVpHCHX6yFnjK9Xt6pG6YBE67PefKPizpCYn2H33XCE7>,
     private_for <xpub6AJDyEAwA8V7nuwxUYCspcTEK99e2JosDFoMs47ZiRt9zNpjsBTvjD9zvFrmTj8Xt5seR7mYh4BMad2DVuqC49BeeKuP6Fgkj3XxHQv8f5Y>]


4. Can also return WIF format:

.. code-block:: python

    >>> xprv.get_child_private_keys(derivation_path='0', index_start=0, index_end=5, wif_format=True)
    ['KykMGuukAqeEnMonWptccpfKpoBfQj7GYQ5wRkktW1Tg2PsK7c4P',
     'KwsnyDdzyggMnR5YwYPL7BytrBDXfVUTJUryF5dqjnqC67cDCkDU',
     'L5L11cqdt8wzssLa5PHxYEYakrQ6NwKgHMVE1DB5uVc3VNjetwZG',
     'L1oYZqnBCUD84qxnatAERsYVa213VCf8ko2Qgr7BbnpMhhMho9qP',
     'L2t4vZE5vHamUcw9knCC97pF7LbqVgAhjAueqGbZVGxyn2ASTaEW']


    >>> # If you only have xpub key you can still generate the addresses to "view only"
    >>> # Use the BitIndex api to query the network directly for xpub total balance etc.
    >>> # xpub queries on BitIndex require an API key from https://www.bitindex.network/#get-api-key

5. A view-only master node (with an xpub key)

.. code-block:: python

    >>> # This is how e.g. handcash, moneybutton, paymail servers generate addresses without ever seeing your private key.
    >>> # First, lets use the xprv master node (from above) to get the xpub!
    >>> xprv.get_xpub()

TODO
----
Complete examples for view-only wallet + ECDSA signatures.