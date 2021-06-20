def Sms():
    import clx.xms

    client = clx.xms.Client('f963ba6222934efea94eff9802d87091', 'b9086b50185b4a5eb885ef4ac4087830')

    batch_params = clx.xms.api.MtBatchTextSmsCreate()
    batch_params.sender = '447537455146'
    batch_params.recipients = {'919352629516'}
    batch_params.body = 'Hello, Mohit !! , We Detected Your Face , Here is Your Image...\nhttp://71d1e6cb6705.ngrok.io/test-img.png\n'
    result = client.create_batch(batch_params)

    print("\n\n Your SMS sent successfully... ")
