# jira-parser
for atlassian jira parser with jira api

## ๐โโ๏ธ What is this?

JIRA์ ์๋ Issue์ ์ฒจ๋ถ ํ์ผ์ ๋ชจ๋ ๋ค์ด๋ก๋ ๋ฐ๊ธฐ ์ํ parser ์๋๋ค.
`issues.txt` ์ํ๋ Issue๋ฅผ line by line์ผ๋ก ๊ธฐ๋กํ๊ณ  ํ ๋ฒ์ ๋ค์ด๋ก๋ ๋ฐ์ ์ ์์ต๋๋ค.

This is a parser to download all attachments of issues in JIRA.
`issues.txt` You can record the desired issues line by line and download them all at once.

## ๐ฒ Usage
1. check JIRA api token info && write your JIRA account info
   - you can access this site => https://id.atlassian.com/manage-profile/security/api-tokens
   - write your info in `setup.conf`
2. write issue items
   - line by line๐
3. run with python3
   ```bash
   python3 attach_downloader.py
   ```
4. play with your `output` directory

## ๐โโ๏ธ TODO
- [ ] check before date with will be download file
- [ ] verify feature for config file
- [ ] convert golang program
