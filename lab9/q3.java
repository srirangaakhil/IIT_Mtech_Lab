import java.util.Scanner;

class q3
{
	public static void main(String[] args)
	{
		int i,j=0,k;
		int a[];
		int flag=2,start=0,end=0;
		Scanner scan = new Scanner(System.in);
		String input = scan.nextLine();
		char[] array=input.toCharArray();
		a = new int[array.length];
		int n = array.length-1;
		for(i=n;i>=0;i--)
		{
			k=Character.getNumericValue(array[i]);
			if(flag==0)
			{
				break;			
			}
			if(k>=0&&k<=9)
			{
				a[j]=k;
				j++;		
			}
			if(array[i]==',')
			{
				a[j]=',';
				j++;	
				flag=flag-1;		
			}
		}
		i=0;
		flag=2;
		j=0;
		k=0;
		while(i<=n)
		{
			if(a[i]==44)
			{
				flag=flag-1;
				i++;
				continue;
			}
			if(flag==1)
			{
				
				if(j==1)
				{
					start=start+(10*a[i]);
				}
				else
				{
					start=start+a[i];
					j=1;
				}
				
			}
			if(flag==2)
			{
				
				if(k==1)
				{
					end=end+(10*a[i]);
				}
				else
				{
					end=end+a[i];
					k=1;
				}
				
			}
			i++;
		}
		
		for(i=start;i<=end;i++)
		{
			System.out.print(array[i]);		
		}
		System.out.println();
	}
}