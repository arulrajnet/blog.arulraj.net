---
title: Generate NATS seed and Keypair using Python nkeys
date: 2024-09-28 09:32
author: arul
category: Python
tags: NATS,Cryptography,PyNacl
slug: generate-nats-seed-and-keypair-using-python-nkeys
disqus_identifier: generate-nats-seed-and-keypair-using-python-nkeys
cover: assets/images/cover-image-nats-python-nkeys.png
color: gray
headline: Python nkeys example for create user, account, server, cluster and operator
status: published
---
This blog post about generate a seed, private_key and public key using Python [nkeys.py](https://github.com/nats-io/nkeys.py)

I couldn't find any direct example to create seed for user, account or cluster as like Golang or Java. 

## 🐎Golang Example

From their [source code](https://github.com/nats-io/nkeys/blob/main/README.md#basic-api-usage) to create new user seed

```go
// Create a new User KeyPair
user, _ := nkeys.CreateUser()

// Access the seed, the only thing that needs to be stored and kept safe.
seed, _ := user.Seed()

// Access the public key which can be shared.
publicKey, _ := user.PublicKey()
```

## ☕Java Example

From their [javadoc](https://javadoc.io/static/io.nats/jnats/2.6.6/io/nats/client/NKey.html) to create new user seed

![[nats-nkey-java-example.png]]
The pseudo code for create user is look like

```java
import io.nats.client.NKey;

NKey nkey = NKey.createUser(null);
System.out.println(nkey.getPublicKey());
System.out.println(nkey.getSeed());
```


The source code is in [here](https://github.com/nats-io/nkeys.java)

## 🐍Python Example

The source code is in [here](https://github.com/nats-io/nkeys.py) . But there is no reference to create user, account or cluster. 

![[nats-nkey-python-example-on-their-repo.png]]

Their documentation talks about from a seed file how we can decode user. Doesn't talks about create new one in anywhere. 

So I have create an example for creating seed for different purposes. 

First of all you have to install nkeys

```bash
pip install nkeys
```
### Create User

Create seed for User

```python
import nkeys
from nacl.signing import SigningKey

signing_key = SigningKey.generate()

# Nats encoded seed for user
src = nkeys.encode_seed(signing_key._seed, prefix=nkeys.PREFIX_BYTE_USER)

# Seed
seed = nkeys.from_seed(src).seed

# Private Key
private_key = nkeys.from_seed(src).private_key

# Public Key
public_key = nkeys.from_seed(src).public_key
```
### Create Account

Create seed for Account

```python
import nkeys
from nacl.signing import SigningKey

signing_key = SigningKey.generate()

# Nats encoded seed for account
src = nkeys.encode_seed(signing_key._seed, prefix=nkeys.PREFIX_BYTE_ACCOUNT)

# Seed
seed = nkeys.from_seed(src).seed

# Private Key
private_key = nkeys.from_seed(src).private_key

# Public Key
public_key = nkeys.from_seed(src).public_key
```
### Create Cluster

Same way just change the prefix for others

Create seed for Cluster

```python
# Nats encoded seed for cluster
src = nkeys.encode_seed(signing_key._seed, prefix=nkeys.PREFIX_BYTE_CLUSTER)
```
### Create Server

Create seed for Server

```python
# Nats encoded seed for server
src = nkeys.encode_seed(signing_key._seed, prefix=nkeys.PREFIX_BYTE_SERVER)
```
### Create Operator

Create seed for Operator

```python
# Nats encoded seed for server
src = nkeys.encode_seed(signing_key._seed, nkeys.PREFIX_BYTE_OPERATOR)
```

You can find all the [prefix](https://github.com/nats-io/nkeys.py/blob/main/nkeys/__init__.py#L24) in their source code.
## 💡How I found

I am always a believer of the show me the code principle. Also we learn more by seeing others code. 

In this [code](https://github.com/nats-io/nkeys.py/blob/main/nkeys/__init__.py#L59) they do padding with given binary array. Also they check the first byte against the predefined byte. Its all start from there. 

## 📖 Learnings in the process

* As you know the keys used by NATS are `ED25519`. There is an python [lib](https://pypi.org/project/ed25519/) for that
* Python Nkeys earlier used that only and they [switch over](https://github.com/nats-io/nkeys.py/pull/4/files) to PyNacl. Since the above lib is not working with latest Python. 
* Lot of the things get from their PyNacl [doc](https://pynacl.readthedocs.io/en/latest/signing/)
* Got to know about [nats-box](https://github.com/nats-io/nats-box) docker and [nsc](https://github.com/nats-io/nsc) command line binary tool available to create creds file and other stuff. 
* The output of seed, private and public key starts with specific prefixes

| Type     | Seed | Private Key | Public Key |
| -------- | ---- | ----------- | ---------- |
| User     | SU   | PC          | UD         |
| Account  | SA   | PC          | AD         |
| Server   | SN   | PC          | ND         |
| Cluster  | SC   | PC          | CD         |
| Operator | SO   | PC          | PO         |
