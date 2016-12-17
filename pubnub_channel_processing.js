// message processing on the pubnub channel
export default (request) => { 
    const pubnub = require('pubnub');
    const kvstore = require('kvstore');
    const xhr = require('xhr');

    console.log(request);
    return request.ok();
}