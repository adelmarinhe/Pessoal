
public class Point extends Object{
	
	private int x; // default value 0
	private int y; // default value 0
		
	// desing by contract
	// invariant de classe [x, y >= 0] [contrato, regra de consistencia]
	
	public Point(int x, int y) {
		if(!isXYNegative(x)) {
			this.x = x;
		}
		if(!isXYNegative(y)) {
			this.y = y;
		}
	}
	
	public int getX() {
		return x;
	}
	
	public void setX(int x) {
		if(!isXYNegative(x)) {
			this.x = x;	
		}
	}
	
	public int getY() {
		return y;
	}
	
	public void setY(int y) {
		if(!isXYNegative(y)) {
			this.y = y;
		}
	}
	
	// helper method
	private boolean isXYNegative(int xy) {
		boolean result = false;
		
		if(xy < 0) {
			result = true;
		}
		
		return result;
	}
}