input=$1
awk '
    {
        for(i=1; i<=NF; i++)
            {
                if(match($i, /^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$/))
                    
                    {
                        print $i
                    }
            }
    }
' $input >out123

awk -F"." '{
if ($1 < 256 && $2 < 256 && $3 < 256 && $4 < 256)
    {
if( $1 <= 127 && $1 >=0)
    {
        print $0 " A"
    }
 if( $1 > 127 && $1 <=191)
      {
         print $0 " B"
      }    
if( $1 > 191 && $1 <=223 )
      {
          print $0 " C"
      } 
      if($1 > 223 && $1 <= 239 )
      {
         print $0 " D"
      } if( $1 > 239 && $1 <=247)
      {
          print $0 " E"
      } if( $1 > 248 && $1 <=255)
      {
          print $0 " Not Defined"
      }

  }

}' out123
rm out123