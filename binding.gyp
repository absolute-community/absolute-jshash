{
    "targets": [
        {
            "target_name": "absolutehash",
            "sources": ["Lyra2RE.c", "Lyra2.c", "Sponge.c",
                        "sha3/blake.c", "sha3/bmw.c", 
                        "sha3/cubehash.c", "sha3/groestl.c", 
                        "sha3/keccak.c", "sha3/skein.c", "scryptn.c",
                        "absolute-hash.cc"],
            "include_dirs" : [ 
                "<!(node -e \"require('nan')\")"
            ]
        }
    ]
}
