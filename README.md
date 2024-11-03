# DES (Data Encryption Standard) Implementation

A pure Python implementation of the DES (Data Encryption Standard) encryption algorithm. This implementation provides a clean, efficient, and easy-to-use interface for DES encryption and decryption without any external dependencies. https://page.math.tu-berlin.de/~kant/teaching/hess/krypto-ws2006/des.htm illustration was used for learning. 

## Features

- Pure Python implementation
- No external dependencies
- Support for variable-length messages
- PKCS#7 padding
- Electronic Codebook (ECB) mode
- Binary data handling

## Installation

Simply copy the `des.py` file into your project directory.



### Working with Different Data Types

Always ideal to operate on raw bytes but strings are also supported. 

## Implementation Details
This needs work.
```mermaid
graph TD
    %% Main Data Flow
    Input[64-bit Input Block] --> InitPerm[Initial Permutation]
    InitPerm --> Split[Split Block]
    Split --> |Left 32 bits| L0[L₀]
    Split --> |Right 32 bits| R0[R₀]
    
    %% Round Structure
    L0 --> |Copy| L1[L₁]
    R0 --> FFunc[F-Function]
    FFunc --> XOR1[⊕]
    L0 --> XOR1
    XOR1 --> R1[R₁]
    
    %% Expansion Details
    R0 --> |32 bits| Expand[Expansion E-Box]
    Expand --> |48 bits| KeyMix[Key Mixing ⊕]
    
    %% S-Box Process
    KeyMix --> SBoxes[8 S-Boxes]
    SBoxes --> |32 bits| Perm[P-Box Permutation]
    Perm --> FOut[F-Function Output]
    
    %% Key Schedule
    Key[64-bit Key Input] --> KeyPerm[Key Permutation PC-1]
    KeyPerm --> |56 bits| Split2[Split Key]
    Split2 --> |28 bits| C0[C₀]
    Split2 --> |28 bits| D0[D₀]
    C0 --> Shift[Left Shift]
    D0 --> Shift
    Shift --> PC2[Permutation PC-2]
    PC2 --> |48-bit Round Key| KeyMix
    
    %% Final Steps
    R1 --> |After 16 rounds| Swap[32-bit Swap]
    L1 --> |After 16 rounds| Swap
    Swap --> FinalPerm[Final Permutation]
    FinalPerm --> Output[64-bit Output Block]
    
    %% Styling
    classDef process fill:#f9f,stroke:#333,stroke-width:2px
    classDef data fill:#bbf,stroke:#333,stroke-width:2px
    classDef key fill:#bfb,stroke:#333,stroke-width:2px
    
    class Input,Output,Key data
    class InitPerm,FinalPerm,SBoxes,Perm,KeyPerm,PC2 process
    class KeyMix,XOR1 key
    
    %% Notes
    subgraph "Key Schedule Process"
        Key
        KeyPerm
        Split2
        Shift
        PC2
    end
    
    subgraph "Main Encryption Flow"
        Input
        InitPerm
        Split
        FFunc
        FinalPerm
        Output
    end
    
    subgraph "F-Function Details"
        Expand
        KeyMix
        SBoxes
        Perm
    end
```

### Key Classes and Methods

#### DES Class

- `__init__(key: bytes)`: Initialize with 8-byte key
- `encrypt(data: bytes) -> bytes`: Encrypt data
- `decrypt(data: bytes) -> bytes`: Decrypt data

### Internal Operations

1. **Key Schedule Generation**
   - Converts 64-bit key to 56 bits (removing parity)
   - Generates 16 48-bit round keys

2. **Block Processing**
   - Initial permutation
   - 16 rounds of Feistel network
   - Final permutation

3. **Padding**
   - PKCS#7 padding for non-64-bit aligned messages
   - Automatically handled during encryption
   - Removed during decryption

## Limitations

- Uses ECB mode only (identical blocks encrypt to identical ciphertext)
- No initialization vector support
- Key must be exactly 8 bytes


## Example Use Cases

### File Encryption

```python
python test.py
```



