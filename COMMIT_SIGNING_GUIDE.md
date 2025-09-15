# Commit Signing Setup Guide

## Why Sign Commits?
- ✅ Verify commit authenticity
- ✅ Prevent commit spoofing
- ✅ Enterprise security compliance
- ✅ Trust and transparency

## Setup Instructions

### 1. Generate GPG Key
```bash
gpg --full-generate-key
# Choose RSA, 4096 bits, no expiration
```

### 2. Configure Git
```bash
# List GPG keys
gpg --list-secret-keys --keyid-format LONG

# Configure Git with your key ID
git config --global user.signingkey YOUR_KEY_ID
git config --global commit.gpgsign true
```

### 3. Add GPG Key to GitHub
```bash
# Export public key
gpg --armor --export YOUR_KEY_ID

# Add to GitHub Settings > SSH and GPG keys
```

### 4. Verify Setup
```bash
# Test signed commit
git commit -S -m "Test signed commit"
```

## Automated Signing
All future commits will be automatically signed when properly configured.

## Troubleshooting
- Ensure GPG agent is running
- Verify key configuration
- Check GitHub GPG key settings
