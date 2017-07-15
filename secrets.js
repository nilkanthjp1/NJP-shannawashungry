var secrets = {
  redis: {
    staging: {
      auth_pass: ""
    },
    me: {
      auth_pass: ""
    },
    production: {
      auth_pass: ""
    }
  },
  s3: {
    accessKeyId:     'AKIAJ7EOV6HYLFV5KSFQ',
    secretAccessKey: '',
  },
  rollbar: {
    development: {
      accessToken: '',
    },
    staging: {
      accessToken: '',
    },
    production: {
      accessToken: '',
    },
  },
};

module.exports = secrets;