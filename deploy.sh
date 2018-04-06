rm -rf docs
cp -r _book docs
git add -A
git commit -m "Automated push"
git push origin master

