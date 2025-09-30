#!/usr/bin/env python3
"""
AlexandrIA Anima Mundi Mail Service
Handles contact form submissions and integrates with the AlexandrIA mail system
"""

import asyncio
import json
import logging
import smtplib
from datetime import datetime
from email.mime.text import MIMEText, MIMEMultipart
from pathlib import Path
import aiohttp
from aiohttp import web, web_request
import aiofiles

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('/home/ichigo/workspace_code/anima-mundi/logs/mail-service.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger('alexandria-mail')

class AlexandriAMailService:
    def __init__(self):
        self.smtp_server = "localhost"  # Will be configured with AlexandrIA mail server
        self.smtp_port = 587
        self.mail_storage = Path("/home/ichigo/workspace_code/anima-mundi/mail-storage")
        self.mail_storage.mkdir(exist_ok=True)
        
    async def save_message(self, message_data: dict) -> str:
        """Save message to local storage for redundancy"""
        timestamp = datetime.now().isoformat()
        filename = f"contact-{timestamp}-{message_data.get('name', 'anonymous').replace(' ', '_')}.json"
        filepath = self.mail_storage / filename
        
        # Add metadata
        message_data.update({
            'received_at': timestamp,
            'service': 'alexandria-anima-mundi-mail',
            'status': 'received'
        })
        
        async with aiofiles.open(filepath, 'w') as f:
            await f.write(json.dumps(message_data, indent=2))
        
        logger.info(f"Message saved to {filepath}")
        return str(filepath)
    
    async def send_notification_email(self, message_data: dict):
        """Send notification email to AlexandrIA team"""
        try:
            # Create email content
            subject = f"[AlexandrIA Contact] {message_data.get('subject', 'New Inquiry')}"
            
            # HTML email template
            html_content = f"""
            <html>
                <body style="font-family: Arial, sans-serif; line-height: 1.6; color: #333;">
                    <div style="max-width: 600px; margin: 0 auto; padding: 20px;">
                        <header style="background: linear-gradient(135deg, #D4AF37, #50C878); color: white; padding: 20px; text-align: center; border-radius: 8px 8px 0 0;">
                            <h1 style="margin: 0;">🏛️ AlexandrIA Anima Mundi</h1>
                            <p style="margin: 5px 0 0;">New Contact Form Submission</p>
                        </header>
                        
                        <div style="background: #f8f9fa; padding: 20px; border: 1px solid #ddd;">
                            <h2 style="color: #D4AF37; border-bottom: 2px solid #D4AF37; padding-bottom: 10px;">Contact Details</h2>
                            
                            <table style="width: 100%; margin-bottom: 20px;">
                                <tr>
                                    <td style="padding: 8px; background: #fff; border: 1px solid #ddd; font-weight: bold; width: 30%;">Name:</td>
                                    <td style="padding: 8px; background: #fff; border: 1px solid #ddd;">{message_data.get('name', 'N/A')}</td>
                                </tr>
                                <tr>
                                    <td style="padding: 8px; background: #fff; border: 1px solid #ddd; font-weight: bold;">Email:</td>
                                    <td style="padding: 8px; background: #fff; border: 1px solid #ddd;">{message_data.get('email', 'N/A')}</td>
                                </tr>
                                <tr>
                                    <td style="padding: 8px; background: #fff; border: 1px solid #ddd; font-weight: bold;">Subject:</td>
                                    <td style="padding: 8px; background: #fff; border: 1px solid #ddd;">{message_data.get('subject', 'N/A')}</td>
                                </tr>
                                <tr>
                                    <td style="padding: 8px; background: #fff; border: 1px solid #ddd; font-weight: bold;">Received:</td>
                                    <td style="padding: 8px; background: #fff; border: 1px solid #ddd;">{message_data.get('timestamp', 'N/A')}</td>
                                </tr>
                            </table>
                            
                            <h3 style="color: #50C878;">Message:</h3>
                            <div style="background: white; padding: 15px; border-left: 4px solid #50C878; margin: 10px 0;">
                                {message_data.get('message', 'No message content')}
                            </div>
                            
                            <hr style="margin: 20px 0; border: none; border-top: 1px solid #ddd;">
                            
                            <p style="text-align: center; color: #666; font-size: 12px;">
                                This message was sent through the AlexandrIA Anima Mundi contact form<br>
                                Preserving humanity's treasures for perpetuity 🌍✨
                            </p>
                        </div>
                    </div>
                </body>
            </html>
            """
            
            # Create message
            msg = MIMEMultipart('alternative')
            msg['Subject'] = subject
            msg['From'] = 'noreply@alexandria.animamundi'
            msg['To'] = 'contact@alexandria.animamundi'
            
            # Attach HTML content
            html_part = MIMEText(html_content, 'html')
            msg.attach(html_part)
            
            # For now, log the email content (will be replaced with actual SMTP when mail server is configured)
            logger.info(f"Email notification prepared: {subject}")
            logger.info(f"Would send to: contact@alexandria.animamundi")
            
            # TODO: Configure SMTP when AlexandrIA mail server is ready
            # with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
            #     server.send_message(msg)
            
            return True
            
        except Exception as e:
            logger.error(f"Failed to send notification email: {e}")
            return False
    
    async def handle_contact_form(self, request: web_request.Request) -> web.Response:
        """Handle contact form submission"""
        try:
            # Parse JSON data
            data = await request.json()
            
            # Validate required fields
            required_fields = ['name', 'email', 'message']
            for field in required_fields:
                if not data.get(field):
                    return web.json_response({
                        'error': f'Missing required field: {field}',
                        'status': 'error'
                    }, status=400)
            
            # Validate email format (basic)
            email = data.get('email')
            if '@' not in email or '.' not in email.split('@')[1]:
                return web.json_response({
                    'error': 'Invalid email format',
                    'status': 'error'
                }, status=400)
            
            # Save message
            filepath = await self.save_message(data)
            
            # Send notification email
            email_sent = await self.send_notification_email(data)
            
            logger.info(f"Contact form submission processed: {data.get('name')} - {data.get('subject')}")
            
            return web.json_response({
                'message': 'Your message has been received successfully. We will get back to you soon!',
                'status': 'success',
                'reference': Path(filepath).name,
                'email_notification': email_sent
            }, status=200)
            
        except json.JSONDecodeError:
            return web.json_response({
                'error': 'Invalid JSON data',
                'status': 'error'
            }, status=400)
        except Exception as e:
            logger.error(f"Error processing contact form: {e}")
            return web.json_response({
                'error': 'Internal server error',
                'status': 'error'
            }, status=500)

async def create_app() -> web.Application:
    """Create and configure the web application"""
    mail_service = AlexandriAMailService()
    
    app = web.Application()
    
    # Add CORS middleware for the frontend
    async def cors_middleware(request: web_request.Request, handler):
        response = await handler(request)
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS'
        response.headers['Access-Control-Allow-Headers'] = 'Content-Type, Authorization'
        return response
    
    app.middlewares.append(cors_middleware)
    
    # Routes
    app.router.add_post('/contact', mail_service.handle_contact_form)
    app.router.add_options('/contact', lambda request: web.Response())
    
    # Health check endpoint
    async def health_check(request: web_request.Request) -> web.Response:
        return web.json_response({
            'service': 'alexandria-anima-mundi-mail',
            'status': 'healthy',
            'timestamp': datetime.now().isoformat()
        })
    
    app.router.add_get('/health', health_check)
    
    return app

async def main():
    """Main application entry point"""
    app = await create_app()
    
    # Start the web server
    runner = web.AppRunner(app)
    await runner.setup()
    
    site = web.TCPSite(runner, '0.0.0.0', 7005)  # Port 7005 for mail service
    await site.start()
    
    logger.info("AlexandrIA Anima Mundi Mail Service started on port 7005")
    
    # Keep the server running
    try:
        await asyncio.Future()  # Run forever
    except KeyboardInterrupt:
        logger.info("Shutting down mail service...")
    finally:
        await runner.cleanup()

if __name__ == '__main__':
    asyncio.run(main())