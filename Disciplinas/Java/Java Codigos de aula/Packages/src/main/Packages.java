package main;

import java.util.*;

import p.c.C;

public class Packages {

	public static void main(String[] args) {
		// ctr + shift + o -> organize imports
		// shortcut
		List v1 = new Vector();
		Vector v2 = new Vector();
		List al = new ArrayList();
		java.awt.List awtList = null;
		
		// importing from different packages
		C c = new C();
		p.h.C c2 = new p.h.C();
	}
}
