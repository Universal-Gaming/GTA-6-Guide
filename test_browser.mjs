#!/usr/bin/env node
// Browser smoke tests for UGN GTA VI Guide. Run with: npm install --no-save playwright && npx playwright install chromium && node test_browser.mjs
import { chromium } from 'playwright';
import { spawn } from 'node:child_process';
import { setTimeout as delay } from 'node:timers/promises';
const port=8765;
const server=spawn('python3',['-m','http.server',String(port),'--bind','127.0.0.1'],{stdio:'ignore'});
const base='http://127.0.0.1:'+port+'/';
let browser;
try {
 await delay(1200);
 browser=await chromium.launch({headless:true});
 const context=await browser.newContext({viewport:{width:390,height:844},acceptDownloads:true});
 const page=await context.newPage();
 const errors=[];
 page.on('pageerror',error=>errors.push(error.message));
 async function visit(path){await page.goto(base+path,{waitUntil:'domcontentloaded'});await page.waitForTimeout(150);if(errors.length)throw Error(path+' browser errors: '+errors.join('; '))}
 await visit('index.html');
 if(await page.locator('#cards a.card').count()!==16)throw Error('Homepage should have 16 working category links');
 await page.locator('#cards a.card').first().click();
 if(!page.url().includes('locations.html'))throw Error('Homepage category navigation failed');
 await visit('encyclopedia.html?category=Vehicles');
 if(await page.locator('#category').inputValue()!=='Vehicles')throw Error('Encyclopedia deep-link filter failed');
 if(await page.locator('#results article').count()<1)throw Error('Encyclopedia filter has no results');
 await visit('progress-vault.html');
 await page.evaluate(()=>localStorage.setItem('ugn-gta6-missions-v1',JSON.stringify(['0-0'])));
 await page.reload();
 const downloadPromise=page.waitForEvent('download');
 await page.locator('#export').click();
 const download=await downloadPromise;
 const stream=await download.createReadStream();
 let json='';for await(const chunk of stream)json+=chunk.toString();
 const backup=JSON.parse(json);
 if(backup.format!=='ugn-gta6-full-backup'||backup.data['ugn-gta6-missions-v1']!=='["0-0"]')throw Error('Full backup missing mission progress');
 await visit('handbook.html');
 if(await page.locator('#cards article').count()!==7)throw Error('Handbook should display seven topics');
 await page.locator('#search').fill('Paradise Taxi');
 if(await page.locator('#cards article').count()!==1)throw Error('Handbook search filter failed');
 await visit('collectibles.html');
 await visit('missions.html');
 await visit('map.html');
 if(errors.length)throw Error('Uncaught browser errors: '+errors.join('; '));
 console.log('PASS: mobile homepage, navigation, encyclopedia filter, vault export, journal, missions and map');
 await context.close();
} finally {if(browser)await browser.close();server.kill();}
