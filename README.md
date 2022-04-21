# jira-parser
for atlassian jira parser with jira api

## 🙋‍♂️ What is this?

JIRA에 있는 Issue의 첨부 파일을 모두 다운로드 받기 위한 parser 입니다.
`issues.txt` 원하는 Issue를 line by line으로 기록하고 한 번에 다운로드 받을 수 있습니다.

This is a parser to download all attachments of issues in JIRA.
`issues.txt` You can record the desired issues line by line and download them all at once.

## 🎲 Usage
1. check JIRA api token info && write your JIRA account info
   - you can access this site => https://id.atlassian.com/manage-profile/security/api-tokens
   - write your info in `setup.conf`
2. write issue items
   - line by line📑
3. run with python3
   ```bash
   python3 attach_downloader.py
   ```
4. play with your `output` directory

## 🏃‍♂️ TODO
- [ ] check before date with will be download file
- [ ] verify feature for config file
- [ ] convert golang program
