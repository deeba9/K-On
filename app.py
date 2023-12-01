from flask import Flask, render_template, request
from flask_mail import Mail, Message


app = Flask(__name__)

# Configure Flask Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = 'deebaumar02@gmail.com'
app.config['MAIL_PASSWORD'] = 'qyujhxxitwwwmvmk'
app.config['MAIL_DEFAULT_SENDER'] = 'your_email@example.com'


mail = Mail(app)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/product')
def product():
    return render_template('blog.html')


@app.route('/subscribe', methods=['POST'])
def subs():
    try:
        em = request.form["email"]
        if em:
            # Print to console (for testing purposes)
            print(em)

            # Append the email to a text file
            save_email(em)

            # You can redirect the user to a thank-you page or the home page
            return render_template("index.html")
    except Exception as e:
        print(e)

    # Handle errors or redirect to the home page
    return render_template("index.html")


def save_email(email):
    # Append the email to the file
    with open("subscribed_emails.txt", "a") as file:
        file.write(email + "\n")


@app.route('/subscribes', methods=['POST'])
def subscribes():
    try:
        name = request.form["name"]
        email = request.form["email"]
        subject = request.form["subject"]
        message = request.form["message"]

        # Set the sender dynamically based on the user's email
        sender = email

        # Compose the email message
        msg = Message(subject, sender=sender, recipients=['deebaumar02@gmail.com'])
        msg.body = f"Name: {name}\nEmail: {email}\nMessage: {message}"

        # Send the email
        mail.send(msg)
        print("Email sent successfully")

        # Return a success message to the frontend
        return render_template("index.html", success=True)

    except Exception as e:
        # Log the error for debugging purposes
        print(f"Error processing form submission: {e}")

        # Return a generic error message to the frontend
        return render_template("index.html", success=False, error_message="An error occurred. Please try again.")


if __name__ == '__main__':
    app.run(debug=True)
