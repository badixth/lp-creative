import React, { useEffect, useRef, useState } from 'react';
import {createRoot} from 'react-dom/client';
import {Input, Switch, Glass, Button} from 'glisse';

const official = 'https://client.loyalprimusmarkets.com';
function Icon({name}) {
  const paths = {
    sun: <><circle cx="12" cy="12" r="4"/><path d="M12 2v2m0 16v2M2 12h2m16 0h2M5 5l1.5 1.5m11 11L19 19M5 19l1.5-1.5m11-11L19 5"/></>,
    moon: <path d="M20 15.5A8.5 8.5 0 0 1 8.5 4 8.5 8.5 0 1 0 20 15.5Z"/>,
    mail: <><rect x="3" y="5" width="18" height="14" rx="3"/><path d="m4 7 7.1 5.1a1.6 1.6 0 0 0 1.8 0L20 7"/></>,
    lock: <><rect x="5" y="10" width="14" height="11" rx="3"/><path d="M8 10V7a4 4 0 0 1 8 0v3"/><path d="M12 14v3"/></>,
    eye: <><path d="M2 12s3.5-6 10-6 10 6 10 6-3.5 6-10 6S2 12 2 12Z"/><circle cx="12" cy="12" r="2.5"/></>,
    hidden: <><path d="m3 3 18 18M9 6.5c6-2 11 3 13 5.5a20 20 0 0 1-3.2 3.6M6 7.3A17 17 0 0 0 2 12s3.5 6 10 6c1.3 0 2.5-.2 3.5-.6"/></>,
    arrow: <path d="M4 12h15m-6-6 6 6-6 6"/>,
    external: <path d="M6 18 18 6M7 6h11v11"/>,
    pause: <><path d="M9 6v12m6-12v12" strokeWidth="2.8"/></>,
    play: <path d="m8 5 10 7-10 7Z" fill="currentColor" stroke="none"/>
  };
  return <svg aria-hidden="true" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.55" strokeLinecap="round" strokeLinejoin="round">{paths[name]}</svg>;
}

function mediaEvent(video, event, ready, signal) {
  if (ready()) return Promise.resolve();
  return new Promise((resolve,reject)=>{
    const clean=()=>{video.removeEventListener(event,done);video.removeEventListener('error',fail);signal.removeEventListener('abort',fail);};
    const done=()=>{if(ready()){clean();resolve();}};
    const fail=()=>{clean();reject(new Error('Media preparation cancelled or unavailable'));};
    video.addEventListener(event,done);video.addEventListener('error',fail);signal.addEventListener('abort',fail,{once:true});
    if(signal.aborted)fail();
  });
}
function Background({theme}) {
  const dark=useRef(null),light=useRef(null),art=useRef(null);
  const initial=useRef(document.documentElement.dataset.theme || 'dark');
  const current=useRef(initial.current),loadedFormat=useRef(null),phase=useRef(0);
  const [visible,setVisible]=useState(initial.current);
  const [format,setFormat]=useState(null);
  const [override,setOverride]=useState(null);
  const [reduced,setReduced]=useState(()=>matchMedia('(prefers-reduced-motion: reduce)').matches);
  const playing=override ?? !reduced;
  useEffect(()=>{
    const media=matchMedia('(prefers-reduced-motion: reduce)');
    const change=event=>setReduced(event.matches);
    media.addEventListener('change',change);return()=>media.removeEventListener('change',change);
  },[]);
  useEffect(()=>{
    let last;
    const fit=()=>{
      const {width,height}=art.current.getBoundingClientRect();
      const ratio=width/height;
      const next=ratio>=1.15?'horizontal':ratio<.66?'vertical':'login';
      if(next!==last){
        const active=current.current==='light'?light.current:dark.current;
        if(active.readyState>=1)phase.current=active.currentTime;
        last=next;setFormat(next);
      }
    };
    const observer=new ResizeObserver(fit);observer.observe(art.current);fit();
    return()=>observer.disconnect();
  },[]);
  useEffect(()=>{
    if(!format)return;
    const controller=new AbortController();let settle;
    const source=current.current==='light'?light.current:dark.current;
    const target=theme==='light'?light.current:dark.current;
    const other=theme==='light'?dark.current:light.current;
    async function prepare(){
      try{
        await mediaEvent(target,'canplay',()=>target.readyState>=2,controller.signal);
        if(controller.signal.aborted)return;
        const time=loadedFormat.current===format && source.readyState>=2 ? source.currentTime : phase.current;
        if(source!==target || loadedFormat.current!==format){
          target.pause();
          const at=time % target.duration;
          if(Math.abs(target.currentTime-at)>.012){
            target.currentTime=at;
            await mediaEvent(target,'seeked',()=>!target.seeking && target.readyState>=2,controller.signal);
          }
        }
        if(controller.signal.aborted)return;
        target.playbackRate=1;
        if(playing)await target.play().catch(()=>{});else{target.pause();other.pause();}
        if(playing && source!==target && loadedFormat.current===format){
          const duration=target.duration;
          const lag=((source.currentTime-target.currentTime+duration/2)%duration+duration)%duration-duration/2;
          target.playbackRate=Math.max(.9,Math.min(1.1,1+lag/.76));
        }
        if(controller.signal.aborted)return;
        current.current=theme;loadedFormat.current=format;
        document.documentElement.dataset.theme=theme;
        try{localStorage.setItem('loyal-primus-theme',theme);}catch{}
        setVisible(theme);
        // Keep both decoded pictures alive during the dissolve, then stop the hidden one.
        settle=setTimeout(()=>{other.pause();target.playbackRate=1;},reduced?0:800);
      }catch(error){if(!controller.signal.aborted)console.warn('Background video unavailable',error);}
    }
    prepare();
    return()=>{controller.abort();clearTimeout(settle);target.playbackRate=1;};
  },[theme,format,playing,reduced]);
  const film=(ref,day)=> <video ref={ref} muted loop playsInline preload="auto"
    src={format?'assets/'+(day?'day-':'')+format+'.mp4?v=studio-day-12s':undefined}
    poster={'assets/'+(day?'day-':'')+(format||'login')+'-poster.webp'}/>;
  return <>
    <div className="scene-layer scene-layer--dark" aria-hidden="true"><div className="art" ref={art}>{film(dark,false)}</div></div>
    <div className="scene-layer scene-layer--light" data-visible={visible==='light'} aria-hidden="true"><div className="art">{film(light,true)}</div></div>
    <Button className="motion" icon={<Icon name={playing?'pause':'play'}/>} aria-label={playing?'Pause animation':'Play animation'} onClick={()=>setOverride(!playing)}/>
  </>;
}

function Login(){
  const [show, setShow] = useState(false);
  const [password, setPassword] = useState('');
  const [complete, setComplete] = useState(false);
  function submit(event) {
    event.preventDefault();
    setPassword('');
    setShow(false);
    setComplete(true);
  }
  return <section className="access" aria-labelledby="sign-in">
    <h1 id="sign-in">Sign in</h1><p className="intro">Sign in to the client portal.</p>
    <form onSubmit={submit} onInput={()=>setComplete(false)}>
      <label htmlFor="account">Email or Account ID</label>
      <Input className="reference-field" icon={<Icon name="mail"/>} id="account" autoComplete="off" autoCapitalize="none" spellCheck={false} required placeholder="name@example.com"/>
      <div className="label-line"><label htmlFor="password">Password</label><a href={official+'/forgot-password'}>Forgot password?</a></div>
      <div className="password">
        <Input className="reference-field" icon={<Icon name="lock"/>} id="password" type={show?'text':'password'} value={password} onValueChange={setPassword} autoComplete="off" required placeholder="Enter your password"/>
        <button className="reveal" type="button" aria-label={show?'Hide password':'Show password'} aria-pressed={show} onClick={()=>setShow(!show)}><Icon name={show?'hidden':'eye'}/></button>
      </div>
      <div className="remember"><label htmlFor="remember">Keep me logged in</label><Switch id="remember" aria-label="Keep me logged in"/></div>
      <Button type="submit" className="submit" variant="filled" tint="#1d9bf0">Login <Icon name="arrow"/></Button>
      {complete && <p role="status" className="status">Form preview complete. <a href={official+'/login'}>Continue to the client portal ↗</a></p>}
    </form>
    <p className="register">New to Loyal Primus? <a href={official+'/register'}>Open an account <Icon name="external"/></a></p>
  </section>;
}
function ThemeToggle({theme,onChange}){
  return <Button className="theme-toggle" icon={<Icon name={theme==='dark'?'sun':'moon'}/>} aria-label={theme==='dark'?'Switch to day mode':'Switch to dark mode'} title={theme==='dark'?'Switch to day mode':'Switch to dark mode'} onClick={()=>onChange(theme==='dark'?'light':'dark')}/>;
}

function Portal(){
  const [theme,setTheme]=useState(()=>document.documentElement.dataset.theme || 'dark');
  return <main className="page">
    <Background theme={theme}/>
    <header><a className="brand" href="https://loyalprimusmarkets.com/" aria-label="Loyal Primus home"><img src="assets/logo-loyalprimus-full.png" width="414" height="33" alt="Loyal Primus"/></a>
      <div className="header-actions"><ThemeToggle theme={theme} onChange={setTheme}/><Glass className="nav-glass"><a className="website" href="https://loyalprimusmarkets.com/">Main website <Icon name="external"/></a></Glass></div></header>
    <section className="identity" aria-label="Loyal Primus"><p className="headline">Trade Better<span>Build Better Future.</span></p>
      <div className="credentials"><img src="assets/asic-regulations.png" alt="ASIC badge"/><i aria-hidden="true"/><img src="assets/fsca-regulations.png" alt="FSCA badge"/></div>
    </section>
    <Login/>
  </main>;
}
createRoot(document.getElementById('app')).render(<Portal/>);
