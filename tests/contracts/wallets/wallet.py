import asyncio
import time

from tonpylib.boc.address import Address
from tonpylib.boc.cell import Cell
from tonpylib.liteclient.client import LiteClient
from tonpylib.tl.block import BlockIdExt
from tonpylib.contract.contract import Contract
from tonpylib.contract.wallets.wallet import WalletV3R2, WalletV3R1, WalletV4R2, Wallet

host = '65.21.141.231'
port = 17728

pub_key_b64 = 'BYSVpL7aPk0kU5CtlsIae/8mf2B/NrBi7DKmepcjX6Q='


async def main():
    client = LiteClient(
        host,
        port,
        pub_key_b64
    )
    await client.connect()

    # m, w = await Wallet.create(provider=client, wc=0, )
    m = ['sea', 'govern', 'comic', 'debate', 'cage', 'reunion', 'oyster', 'electric', 'mean', 'rabbit', 'display', 'mom',
     'ignore', 'lake', 'path', 'people', 'lobster', 'rigid', 'canyon', 'trash', 'elephant', 'scissors', 'brisk',
     'insane']
    new_w = await Wallet.from_mnemonic(provider=client, mnemonics=m)
    print(new_w)

    # await new_w.deploy_via_external()
    # await w.transfer(destination=Address('EQAXA8eBIhU3Jlsd0ydlqfSMrB7Sqigdgh4pLmQJ_kb9DHg9').to_str(is_user_friendly=True, is_bounceable=False), amount=1 * 10**7, body='hello')

    c = await Contract.from_address(client, Address((0, b'o[\xc6y\x86\xe0d0\x96\x1d\x9d\xf0\x043\x92jL\xd9.Y}\xdd\x8a\xa6\x046E\xac \xbd\x17\x83')))
    print(c)
    print(c.is_uninitialized)

    wallet = await WalletV3R2.from_address(provider=client, address='EQCA1BI4QRZ8qYmskSRDzJmkucGodYRTZCf_b9hckjla6dZl')
    print(wallet)
    print(await wallet.get_seqno())
    print(wallet.seqno)
    print(wallet.public_key)
    print(await wallet.get_public_key())

    wallet2 = await WalletV3R1.from_address(provider=client, address='EQBVXzBT4lcTA3S7gxrg4hnl5fnsDKj4oNEzNp09aQxkwj1f')
    print(await wallet2.get_seqno())
    print(wallet2.seqno)
    print(wallet2.public_key)
    # print(await wallet2.get_public_key())

    wallet3 = await WalletV4R2.from_address(provider=client, address='EQBvW8Z5huBkMJYdnfAEM5JqTNkuWX3diqYENkWsIL0XggGG')

    print(await wallet3.get_seqno())
    print(wallet3.seqno)
    print(wallet3.public_key)
    print(await wallet3.get_public_key())
    print(wallet3.plugins)
    print(await wallet3.get_plugin_list())
    print(await wallet3.is_plugin_installed(address=Address('EQBvW8Z5huBkMJYdnfAEM5JqTNkuWX3diqYENkWsIL0XggGG')))


if __name__ == '__main__':
    asyncio.run(main())