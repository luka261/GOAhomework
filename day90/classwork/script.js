class UserProfile {
    #username;
    #email;
    #password;
  
    constructor(username, email, password) {
      this.#username = username;
      this.#email = email;
      this.#password = password;
    }
  
    validatePassword(password) {
      return password === this.#password;
    }
  
    updateEmail(newEmail) {
      if (newEmail.includes("@")) {
        this.#email = newEmail;
      }
    }
  
    updatePassword(newPassword) {
      if (newPassword.length >= 6) {
        this.#password = newPassword;
      }
    }
  
    getUsername() {
      return this.#username;
    }
  }
  
  class Car {
    #engineStatus;
    #speed;
    #fuelLevel;
  
    constructor(fuelLevel) {
      this.#engineStatus = false;
      this.#speed = 0;
      this.#fuelLevel = fuelLevel;
    }
  
    startEngine() {
      if (this.#fuelLevel > 0) {
        this.#engineStatus = true;
      }
    }
  }
  
