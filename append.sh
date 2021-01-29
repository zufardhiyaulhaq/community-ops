for f in *.yaml
do 
cat << EOF >> $f
status:
  send: true
EOF
done
