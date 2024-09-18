class q1
{
	public static void main(String[] args) 
  	{
		int sum=0;
		int product=1,i;
		for(i=0;i<args.length;i++)
		{
			sum=sum+Integer.parseInt(args[i]);
			product=product*Integer.parseInt(args[i]);		
		}
		System.out.println(args.length+","+sum+","+product);
  	}
}