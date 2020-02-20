/*
 * this program takes a 3 digit number as input from the user
 * then generates a 3 digit number by itself
 * if the users input number matches the CPU's generated number
 * 	then the user wins a prize
 */
import java.util.Scanner;//imported scanner from java.util so the user can input a value
public class threeDigitLot {

	public static void main(String[] args) {
		
		System.out.println("Welcome to 3-Digit Lottery Program");//welcome string
		System.out.println("Play to get a chance to win $10,000!!!");//tells the user what the program is about
		
		System.out.println("Please enter a 3-didgit number:");//asks the user to input a 3-digit value
		
		Scanner input = new Scanner(System.in);//this is the scanner, which is what creates the input 
		
		int userNum = input.nextInt();//this tells the program to take as input the next inputed integer
		
		boolean validInput = false;//boolean to check if the input value is valid or not
		
		if(userNum == 000)//this is the probability of getting a 3-digit input value of 3 zeros
			validInput = true;//if the statement above gets inputed than it should be valid
		else if(userNum < 100 || userNum > 999)//statement tells the program that 2-digit values are not valid
			validInput = false;//invalid input
		else//any 3-digit values will be accepted between 100-999
			validInput = true;//valid input
		
		if(validInput)//in the case that the input value is valid the program will run the statements below
		{
			double lotRand = Math.random();//generates a random number from 0-1
			
			int lotNum = (int)(lotRand * 899 + 100);//then that number generated gets multiplied by 899 and then added 100 
			//so that the value gets converted to an integer value between 100-999 
			
			//here the program will gather the separate digits from both the input and the lottery number to be compared
			int lotXY = lotNum / 10;//gets the first 2 digits of the lottery number 
			int userAB = userNum / 10;//gets the first 2 digits of the user input number 
			
			//finding the xyz of the lottery number
			int lotX = lotNum / 100;//gets the 1st value of the lottery number
			int lotY = lotXY % 10;//gets the 2nd value of the lottery number
			int lotZ = lotNum % 10;//gets the 3rd value of the lottery number
			
			//finding the xyz of the user input number
			int uNumX = userNum / 100;//gets the 1st value of the user input number
			int uNumY = userAB % 10;//gets the 2nd value of the user input number
			int uNumZ = userNum % 10;//gets the 3rd value of the user input number
			
			//changing the variables to more simpler ones
			//abc = user's input number's digits 
			//xyz = lottery/generated number's digits 
			//lottery's
			int x = lotX;//1st digit
			int y = lotY;//2nd digit
			int z = lotZ;//3rd digit
			//user's
			int a = uNumX;//1st digit
			int b = uNumY;//2nd digit
			int c = uNumZ;//3rd digit
			
		//perfect match
		//in the case that all the digits match in the right order 
		if(userNum == lotNum) {
			System.out.println("You matched all the numbers in exact order \n"//tells the user how many digits they matched
					+ "You Win $10,000!!!");//tells the user the prize won 
		}
		//matching all numbers but in different order
		//in the case that the user matches all the digits but in a different order
		else if((a == x && b == z && c == y) || (a == y && b == x && c == z) || (a == y && b == z && c == x) //list of possibilities 
				|| (a == y && b == z && c == x) || (a == z && b == y && c == x) || (a == z && b == x && c == y)) {
			System.out.println("You matched all the numbers in different order \n"//tells the user how many digits they matched
					+ "You win $7,000!!!");//tells the user the prize won 
		}
		//only 2 numbers match
		//in the case of the user only matching 2 digits from the 3-digit lottery number
		else if((a == x && b == y) || (a == x && b == z) || (a == y && b == z) //list of all possibilities
				|| (a == x && c == z) || (a == y && c == z ) || (a == x && c == y)
				|| (b == y && c == z) || (b == x && c == z) || (b == x && c == y)
				|| (b == y && a == z) || (b == x && a == z) || (b == x && a == y)
				|| (c == y && a == z) || (c == x && a == z) || (c == x && a == y)
				|| (c == y && b == z) || (c == x && b == z) || (c == x && b == y)){
			System.out.println("You matched at two numbers \n"//tells the user how many digits they matched
					+ "You win $4,000!!!");//tells the user the prize won 
		}
		//only 1 number match
		//in the case of the user only matching 1 digits from the 3-digit lottery number
		else if((a == x) || (a == y) || ( a == z)
				||(b == x) || (b == y) || (b == z)
				|| (c == x) || (c == y) || (c == z)) {
			System.out.println("You matched only one digit \n"//tells the user how many digits they matched
					+ "You win $1,000!!!");//tells the user the prize won 
		}
		//no match
		//in the case of the user not matching any digits from the 3-digit lottery number
		else
			System.out.println("You did not matched any number \n"//tells the user how many digits they matched
					+ "Goodluck next time!");//tells the user the prize won 
		}
		//wrong input
		else
			System.out.println("Invalid Input");//this statement get printed out if there is an invalid input value
		
		
		
		
		
		

	}

}
