//Kevin Suarez
import java.util.Scanner;//imports scanner from java.util so that an user input can be created 
public class nestedLoopAssign {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		System.out.println("Welcome to program that creates a nested loop with a design!");//weclome string

		Scanner input = new Scanner(System.in);//creates the user input so that the user can input a value asked
		
		System.out.println("Please enter the number of rows:");//tells the user what to input
		
		int n = input.nextInt();//creates a variable to store the value entered by the user
								
		for (int i = 0; i < n; i++) {//is the outer loop which prints out the "y's" in a coordinate plane 
			for (int j = 1; j < n-i ;j++) {//is the inner loop which prints out the "x's" in a coordinate plane
				System.out.print("!");//prints the ! symbol
			}
			for(int k = 0; k <= i; k++) {//loop that tells where the * will be at (which coordinates will they be at)
				System.out.print("*");//prints out the * symbol
			}
		System.out.println();//makes everything print out line by line instead of just one line
		}
		
		
	}
}


