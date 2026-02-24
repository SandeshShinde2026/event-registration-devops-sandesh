from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        event = request.form['event']
        return f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Success - Event Registration</title>
            <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
            <style>
                :root {{
                    --bg: #09090b;
                    --surface: #18181b;
                    --text-primary: #f4f4f5;
                    --text-secondary: #a1a1aa;
                    --accent: #22c55e;
                }}
                
                body {{
                    font-family: 'Plus Jakarta Sans', sans-serif;
                    background-color: var(--bg);
                    color: var(--text-primary);
                    min-height: 100vh;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    margin: 0;
                    padding: 1rem;
                }}

                /* Decorative Grid Background */
                body::before {{
                    content: "";
                    position: absolute;
                    inset: 0;
                    background-image: 
                        linear-gradient(rgba(255, 255, 255, 0.03) 1px, transparent 1px),
                        linear-gradient(90deg, rgba(255, 255, 255, 0.03) 1px, transparent 1px);
                    background-size: 32px 32px;
                    mask-image: radial-gradient(circle at center, black 40%, transparent 100%);
                    z-index: -1;
                    pointer-events: none;
                }}

                .success-card {{
                    background: var(--surface);
                    padding: 3rem;
                    border-radius: 16px;
                    border: 1px solid #3f3f46;
                    text-align: center;
                    max-width: 500px;
                    width: 100%;
                    box-shadow: 0 0 0 1px rgba(0,0,0,0.4), 0 20px 40px -12px rgba(0,0,0,0.5);
                    animation: slideUp 0.6s cubic-bezier(0.16, 1, 0.3, 1);
                }}

                .icon {{
                    font-family: 'JetBrains Mono', monospace;
                    font-size: 0.875rem;
                    color: var(--accent);
                    margin-bottom: 1.5rem;
                    display: inline-block;
                    padding: 0.5rem 1rem;
                    background: rgba(34, 197, 94, 0.1);
                    border-radius: 9999px;
                    border: 1px solid rgba(34, 197, 94, 0.2);
                }}

                h2 {{
                    font-size: 2rem;
                    margin-bottom: 0.5rem;
                    font-weight: 700;
                    letter-spacing: -0.02em;
                }}

                p {{
                    color: var(--text-secondary);
                    line-height: 1.6;
                    margin-bottom: 2.5rem;
                    font-size: 1.125rem;
                }}

                b {{
                    color: var(--text-primary);
                    font-weight: 600;
                }}

                .btn {{
                    display: block;
                    width: 100%;
                    padding: 1rem;
                    background: var(--text-primary);
                    color: var(--bg);
                    text-decoration: none;
                    border-radius: 8px;
                    font-weight: 600;
                    transition: opacity 0.2s;
                }}

                .btn:hover {{
                    opacity: 0.9;
                }}

                @keyframes slideUp {{
                    from {{ opacity: 0; transform: translateY(20px); }}
                    to {{ opacity: 1; transform: translateY(0); }}
                }}
            </style>
        </head>
        <body>
            <div class="success-card">
                <div class="icon">● STATUS: CONFIRMED</div>
                <h2>You're In.</h2>
                <p>Registration for <b>{name}</b> has been locked in for the <b>{event}</b> track. Details sent to <b>{email}</b>.</p>
                <a href="/" class="btn">Register Another Attendee</a>
            </div>
        </body>
        </html>
        """
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)