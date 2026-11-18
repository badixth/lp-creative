from pathlib import Path
import json
O=Path(__file__).resolve().parents[1];P=O.parent
COPY={
 'subject':'A personal note from your Loyal Primus team',
 'preheader':'Thank you for being part of Loyal Primus. A few words from our team to you.',
 'greeting':'Hi {{first_name}},',
 'paragraphs':[
  'Thank you for making Loyal Primus part of your trading journey. We wanted to take a moment to tell you how much we appreciate the trust you place in us.',
  'Every client approaches the markets differently. Whether you’re reviewing your account, exploring its features or looking for an answer, we want the information you receive from us to be clear and useful.',
  'If there’s something you’d like to discuss, we’re here to help. Visit your client area for your account information, or get in touch with our team. We’d be glad to hear from you.'
 ],
 'signoff':'Warm regards,','sender':'Your Loyal Primus team','cta':'Visit your client area',
 'cta_url':'https://client.loyalprimusmarkets.com/','status':'Sample personal-message copy for layout review; replace with the real client message.'
}
if (O/'copy.json').exists():COPY=json.loads((O/'copy.json').read_text())
else:(O/'copy.json').write_text(json.dumps(COPY,indent=2,ensure_ascii=False))
(O/'email.txt').write_text(COPY['greeting']+'\n\n'+'\n\n'.join(COPY['paragraphs'])+'\n\n'+COPY['signoff']+'\n'+COPY['sender']+'\n\n'+COPY['cta']+': '+COPY['cta_url']+'\n\nSupport: https://loyalprimusmarkets.com/contact-us/\n\nLeveraged trading involves risk and can result in significant losses.\nUnsubscribe: {{unsubscribe_url}}\n{{sender_postal_address}}\n')
styles='''body{margin:0!important;padding:0!important;width:100%!important;background:#080b10;-webkit-text-size-adjust:100%;-ms-text-size-adjust:100%}table{border-collapse:collapse;mso-table-lspace:0;mso-table-rspace:0}td{padding:0;font-family:Arial,Helvetica,sans-serif}img{display:block;border:0;outline:0}h1,h2,p{margin:0}a{color:inherit}a[x-apple-data-detectors]{color:inherit!important;text-decoration:none!important}@media screen and (max-width:520px){.feature-section{padding:0!important}.feature-gap{width:10px!important}.reward-title{padding:17px 13px 0!important}.reward-title h3{font-size:19px!important;line-height:23px!important}.reward-art{padding:25px 0 0!important}.small-panel{height:137px!important}.small-copy{display:block!important;width:auto!important;padding:12px 12px 0!important}.small-title{font-size:13px!important;line-height:17px!important;letter-spacing:-.2px!important}.small-title span{display:inline!important}.small-arrow{display:none!important}.small-art{display:block!important;width:100%!important}.small-art img{width:104px!important;max-width:104px!important}.stack-gap{height:10px!important;line-height:10px!important}.shell{width:100%!important}.outer{padding:0!important}.mast{padding:27px 27px 0!important}.mast-logo{width:155px!important}.mast-note{font-size:8px!important;letter-spacing:1.1px!important}.hero-type{padding:37px 20px 28px!important}.hero-first{font-size:46px!important;line-height:52px!important;letter-spacing:-1.6px!important}.hero-second{font-size:30px!important;line-height:38px!important;letter-spacing:-.7px!important}.hero-caption{font-size:11px!important;padding-top:18px!important}.reading{padding:36px 28px 40px!important}.letter-lead{font-size:27px!important;line-height:34px!important}.letter-copy{font-size:15px!important;line-height:25px!important}.closing{padding:33px 28px 5px!important}.closing-title{font-size:27px!important;line-height:34px!important;letter-spacing:-.8px!important}.signature-label{font-size:9px!important}.footer{padding:35px 28px 30px!important}.footer-logo{width:205px!important}.legal{font-size:10px!important;line-height:16px!important}.preheader-view{padding:12px 20px!important}.reply-link{padding-top:13px!important;display:block!important}}'''
paras=''.join(f'<p class="letter-copy" style="margin:0 0 21px;font-size:16px;line-height:27px;color:#FFFFFF;">{p}</p>' for p in COPY['paragraphs'])
html=f'''<!doctype html><html lang="en" xmlns:v="urn:schemas-microsoft-com:vml" xmlns:o="urn:schemas-microsoft-com:office:office"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="color-scheme" content="light"><meta name="supported-color-schemes" content="light"><title>Loyal Primus · A personal note</title><!--[if mso]><xml><o:OfficeDocumentSettings><o:AllowPNG/><o:PixelsPerInch>96</o:PixelsPerInch></o:OfficeDocumentSettings></xml><![endif]--><style>{styles}</style></head><body>
<div style="display:none;max-height:0;overflow:hidden;opacity:0;font-size:1px;line-height:1px;mso-hide:all;">{COPY['preheader']}&#847;&zwnj;&#847;&zwnj;</div>
<table role="presentation" width="100%"><tr><td class="outer" align="center" style="padding:24px 0;">
<!--[if mso]><table role="presentation" width="600"><tr><td><![endif]-->
<table role="presentation" class="shell" width="600" style="width:600px;max-width:600px;" bgcolor="#000102">
<tr><td class="preheader-view" align="center" style="padding:0 20px 16px;background:#080b10;font-size:9px;line-height:13px;color:#FFFFFF;"><a href="{{{{view_in_browser_url}}}}" style="text-decoration:underline;">View this letter in your browser</a></td></tr>
<tr><td align="center" bgcolor="#000000" style="padding:4% 0 0;background:#000000;font-size:0;line-height:0;"><img src="assets/logo.png" alt="Loyal Primus" width="200" style="display:block;width:33.333333%;max-width:200px;height:auto;margin:0 auto;"></td></tr>
<tr><td bgcolor="#000000" style="padding:0;background:#000000;"><h1 style="margin:0;font-size:0;line-height:0;font-weight:normal;"><img src="assets/hero-compact.jpg" alt="Trade Better, Build Brighter Future." width="600" style="width:100%;height:auto;display:block;"></h1></td></tr>
<tr><td class="reading" bgcolor="#000000" style="padding:40px 48px 40px;background:#000000;">
<h2 class="letter-lead" style="margin:0 0 27px;font-family:Arial,Helvetica,sans-serif;font-size:30px;line-height:37px;letter-spacing:-1px;font-weight:bold;color:#FFFFFF;">A personal thank you.</h2>
<p class="letter-copy" style="margin:0 0 21px;font-size:16px;line-height:27px;color:#FFFFFF;">{COPY['greeting']}</p>
{paras}
<p style="padding-top:3px;font-size:14px;line-height:23px;color:#FFFFFF;">{COPY['signoff']}<br><strong style="font-weight:normal;font-family:Arial,Helvetica,sans-serif;font-size:17px;line-height:29px;font-style:normal;color:#FFFFFF;">{COPY['sender']}</strong></p>
<table role="presentation" style="margin-top:28px;"><tr><td bgcolor="#087DCE" style="border:0;border-radius:24px;background:#087DCE;"><a href="{COPY['cta_url']}" target="_blank" style="display:inline-block;padding:14px 25px;font-size:13px;line-height:18px;color:#FFFFFF;text-decoration:none;font-weight:bold;border-radius:24px;mso-padding-alt:0;"><!--[if mso]><i style="letter-spacing:25px;mso-font-width:-100%;mso-text-raise:20pt;">&nbsp;</i><![endif]-->{COPY['cta']}<!--[if mso]><i style="letter-spacing:25px;mso-font-width:-100%;">&nbsp;</i><![endif]--></a></td></tr></table>
<p style="margin-top:17px;font-size:11px;line-height:18px;color:#FFFFFF;">Need a hand? <a href="https://loyalprimusmarkets.com/contact-us/" style="color:#FFFFFF;text-decoration:underline;">Talk to our team</a>.</p>
</td></tr>
<tr><td class="feature-section" bgcolor="#000000" style="padding:0;background:#000000;">
<table role="presentation" width="100%" cellspacing="0" cellpadding="0" border="0" style="table-layout:fixed;border-collapse:collapse;"><tr>
<td width="50%" valign="top" style="padding:0;font-size:0;line-height:0;"><a href="https://loyalprimusmarkets.com/loyalty-program/"><img src="assets/feature-left.jpg" alt="Loyalty Points — Get Exclusive Rewards" width="300" style="width:100%;height:auto;display:block;"></a></td>
<td width="50%" valign="top" style="padding:0;font-size:0;line-height:0;"><table role="presentation" width="100%" cellspacing="0" cellpadding="0" border="0"><tr><td style="padding:0;font-size:0;line-height:0;"><a href="https://loyalprimusmarkets.com/our-pricing-plans/"><img src="assets/feature-top-right.jpg" alt="Leverage up to 1:2000" width="300" style="width:100%;height:auto;display:block;"></a></td></tr><tr><td style="padding:0;font-size:0;line-height:0;"><a href="https://loyalprimusmarkets.com/our-pricing-plans/"><img src="assets/feature-bottom-right.jpg" alt="Spread from 0 pips" width="300" style="width:100%;height:auto;display:block;"></a></td></tr></table></td>
</tr></table></td></tr>
<tr><td height="3" bgcolor="#000000" style="height:3px;font-size:1px;line-height:3px;">&nbsp;</td></tr>
<tr><td class="footer" align="center" bgcolor="#000000" style="padding:35px 44px 28px;background:#000000;">
<img class="footer-logo" src="assets/logo.png" alt="Loyal Primus" width="230" style="width:230px;height:auto;margin:0 auto;">

<p style="margin-top:17px;font-size:12px;line-height:21px;color:#FFFFFF;"><a href="https://loyalprimusmarkets.com/contact-us/" style="text-decoration:none;font-weight:bold;">Contact our team</a><span style="color:#FFFFFF;"> &nbsp;&nbsp; | &nbsp;&nbsp; </span><a href="https://client.loyalprimusmarkets.com/" style="text-decoration:none;font-weight:bold;">Client area</a></p>
<table role="presentation" width="100%" style="margin-top:25px;"><tr><td height="1" bgcolor="#252525" style="height:1px;font-size:1px;line-height:1px;">&nbsp;</td></tr></table>
<p style="margin-top:23px;color:#FFFFFF;font-size:11px;line-height:20px;">© 2026 Loyal Primus. All rights reserved.</p>
<p style="margin-top:9px;color:#FFFFFF;font-size:11px;line-height:23px;"><a href="{{{{unsubscribe_url}}}}" style="text-decoration:underline;">Unsubscribe</a> &nbsp; · &nbsp; <a href="https://loyalprimusmarkets.com/terms-of-business/" style="text-decoration:underline;">Terms of Business</a> &nbsp; · &nbsp; <a href="https://loyalprimusmarkets.com/privacy-policy/" style="text-decoration:underline;">Privacy Policy</a></p>
<p style="margin-top:8px;color:#FFFFFF;font-size:10px;line-height:17px;"><a href="{{{{preferences_url}}}}" style="text-decoration:underline;">Manage email preferences</a></p>
</td></tr>
<tr><td class="legal-panel" bgcolor="#000000" style="padding:24px 36px 26px;">
<p class="legal" style="color:#FFFFFF;font-size:10px;line-height:17px;text-align:center;">Leveraged trading involves risk and can result in significant losses. Account conditions and rewards are subject to eligibility, availability and applicable terms.</p>
<p style="margin-top:12px;color:#FFFFFF;font-size:9px;line-height:15px;text-align:center;">{{{{sender_postal_address}}}}</p>
</td></tr></table><!--[if mso]></td></tr></table><![endif]-->
</td></tr></table></body></html>'''
(O/'email.html').write_text(html)
section_start=html.index('<tr><td class="feature-section"')
section_end=html.index('<tr><td height="3"',section_start)
(O/'section-email.html').write_text('<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Loyal Primus · Account section</title><style>'+styles+'</style></head><body style="background:#080F19;"><table role="presentation" class="shell" width="600" style="width:600px;max-width:600px;margin:0 auto;">'+html[section_start:section_end]+'</table></body></html>')
preview=html.replace('{{first_name}}','Alex').replace('{{view_in_browser_url}}','email-preview.html').replace('{{preferences_url}}','#delivery-settings').replace('{{unsubscribe_url}}','#delivery-settings').replace('{{sender_postal_address}}','Loyal Primus · Client communications')
preview=preview.replace('</body>','''<script>function report(){parent.postMessage({type:'email-height',height:document.documentElement.scrollHeight},'*')}addEventListener('load',report);new ResizeObserver(report).observe(document.body);document.querySelectorAll('a[href="#delivery-settings"]').forEach(a=>a.addEventListener('click',e=>{e.preventDefault();parent.postMessage({type:'delivery-note'},'*')}));</script></body>''')
(O/'email-preview.html').write_text(preview)
wrapper=(O/'preview.html').read_text().replace('Full email · layout preview v1','Trade Better · refined v3').replace('position:sticky;top:0','position:relative;top:0').replace('Dark edition · complete gift ribbon','Dark edition · compact header').replace('Design preview with live copy and links. Delivery fields are reserved for your email platform.','Sample personal letter for existing clients. Body copy, greeting and sign-off are editable. Delivery fields are reserved for your email platform.')
(O/'preview.html').write_text(wrapper)
print('V28 built',len(html.encode()),'bytes')
