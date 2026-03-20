true = True
false = False


# taken from the example queries on the api website
TICKET_MASTER_EVENT_SEARCH_MOCK = {
  "_links":  {
    "self":  {
      "href": "/discovery/v2/events.json?size=1{&page,sort}",
      "templated": true
    },
    "next":  {
      "href": "/discovery/v2/events.json?page=1&size=1{&sort}",
      "templated": True
    }
  },
  "_embedded":  {
    "events":  [
       {
        "name": "WGC Cadillac Championship - Sunday Ticket",
        "type": "event",
        "id": "vvG1VZKS5pr1qy",
        "test": False,
        "url": "http://ticketmaster.com/event/0E0050681F51BA4C",
        "locale": "en-us",
        "images":  [
           {
            "ratio": "16_9",
            "url": "http://s1.ticketm.net/dam/a/196/6095e742-64d1-4b15-aeac-c9733c52d196_66341_RETINA_LANDSCAPE_16_9.jpg",
            "width": 1136,
            "height": 639,
            "fallback": False
          },
           {
            "ratio": "3_2",
            "url": "http://s1.ticketm.net/dam/a/196/6095e742-64d1-4b15-aeac-c9733c52d196_66341_RETINA_PORTRAIT_3_2.jpg",
            "width": 640,
            "height": 427,
            "fallback": False
          },
           {
            "ratio": "16_9",
            "url": "http://s1.ticketm.net/dam/a/196/6095e742-64d1-4b15-aeac-c9733c52d196_66341_TABLET_LANDSCAPE_LARGE_16_9.jpg",
            "width": 2048,
            "height": 1152,
            "fallback": False
          },
           {
            "ratio": "16_9",
            "url": "http://s1.ticketm.net/dam/a/196/6095e742-64d1-4b15-aeac-c9733c52d196_66341_TABLET_LANDSCAPE_16_9.jpg",
            "width": 1024,
            "height": 576,
            "fallback": False
          },
           {
            "ratio": "16_9",
            "url": "http://s1.ticketm.net/dam/a/196/6095e742-64d1-4b15-aeac-c9733c52d196_66341_EVENT_DETAIL_PAGE_16_9.jpg",
            "width": 205,
            "height": 115,
            "fallback": False
          },
           {
            "ratio": "3_2",
            "url": "http://s1.ticketm.net/dam/a/196/6095e742-64d1-4b15-aeac-c9733c52d196_66341_ARTIST_PAGE_3_2.jpg",
            "width": 305,
            "height": 203,
            "fallback": False
          },
           {
            "ratio": "16_9",
            "url": "http://s1.ticketm.net/dam/a/196/6095e742-64d1-4b15-aeac-c9733c52d196_66341_RETINA_PORTRAIT_16_9.jpg",
            "width": 640,
            "height": 360,
            "fallback": False
          },
           {
            "ratio": "4_3",
            "url": "http://s1.ticketm.net/dam/a/196/6095e742-64d1-4b15-aeac-c9733c52d196_66341_CUSTOM.jpg",
            "width": 305,
            "height": 225,
            "fallback": False
          },
           {
            "ratio": "16_9",
            "url": "http://s1.ticketm.net/dam/a/196/6095e742-64d1-4b15-aeac-c9733c52d196_66341_RECOMENDATION_16_9.jpg",
            "width": 100,
            "height": 56,
            "fallback": False
          },
           {
            "ratio": "3_2",
            "url": "http://s1.ticketm.net/dam/a/196/6095e742-64d1-4b15-aeac-c9733c52d196_66341_TABLET_LANDSCAPE_3_2.jpg",
            "width": 1024,
            "height": 683,
            "fallback": False
          }
        ],
        "sales":  {
          "public":  {
            "startDateTime": "2015-10-02T11:00:00Z",
            "startTBD": False,
            "endDateTime": "2016-03-06T23:00:00Z"
          }
        },
        "dates":  {
          "start":  {
            "localDate": "2016-03-06",
            "dateTBD": False,
            "dateTBA": False,
            "timeTBA": True,
            "noSpecificTime": False
          },
          "timezone": "America/New_York",
          "status":  {
            "code": "offsale"
          }
        },
        "classifications":  [
           {
            "primary": True,
            "segment":  {
              "id": "KZFzniwnSyZfZ7v7nE",
              "name": "Sports"
            },
            "genre":  {
              "id": "KnvZfZ7vAdt",
              "name": "Golf"
            },
            "subGenre":  {
              "id": "KZazBEonSMnZfZ7vFI7",
              "name": "PGA Tour"
            }
          }
        ],
        "promoter":  {
          "id": "682"
        },
        "_links":  {
          "self":  {
            "href": "/discovery/v2/events/vvG1VZKS5pr1qy?locale=en-us"
          },
          "attractions":  [
             {
              "href": "/discovery/v2/attractions/K8vZ917uc57?locale=en-us"
            }
          ],
          "venues":  [
             {
              "href": "/discovery/v2/venues/KovZpZAaEldA?locale=en-us"
            }
          ]
        },
        "_embedded":  {
          "venues":  [
             {
              "name": "Trump National Doral",
              "type": "venue",
              "id": "KovZpZAaEldA",
              "test": False,
              "locale": "en-us",
              "postalCode": "33178",
              "timezone": "America/New_York",
              "city":  {
                "name": "Miami"
              },
              "state":  {
                "name": "Florida",
                "stateCode": "FL"
              },
              "country":  {
                "name": "United States Of America",
                "countryCode": "US"
              },
              "address":  {
                "line1": "4400 NW 87th Avenue"
              },
              "location":  {
                "longitude": "-80.33854298",
                "latitude": "25.81260379"
              },
              "markets":  [
                 {
                  "id": "15"
                }
              ],
              "_links":  {
                "self":  {
                  "href": "/discovery/v2/venues/KovZpZAaEldA?locale=en-us"
                }
              }
            }
          ],
          "attractions":  [
             {
              "name": "Cadillac Championship",
              "type": "attraction",
              "id": "K8vZ917uc57",
              "test": False,
              "locale": "en-us",
              "images":  [
                 {
                  "ratio": "16_9",
                  "url": "http://s1.ticketm.net/dam/a/196/6095e742-64d1-4b15-aeac-c9733c52d196_66341_RETINA_LANDSCAPE_16_9.jpg",
                  "width": 1136,
                  "height": 639,
                  "fallback": False
                },
                 {
                  "ratio": "3_2",
                  "url": "http://s1.ticketm.net/dam/a/196/6095e742-64d1-4b15-aeac-c9733c52d196_66341_RETINA_PORTRAIT_3_2.jpg",
                  "width": 640,
                  "height": 427,
                  "fallback": False
                },
                 {
                  "ratio": "16_9",
                  "url": "http://s1.ticketm.net/dam/a/196/6095e742-64d1-4b15-aeac-c9733c52d196_66341_TABLET_LANDSCAPE_LARGE_16_9.jpg",
                  "width": 2048,
                  "height": 1152,
                  "fallback": False
                },
                 {
                  "ratio": "16_9",
                  "url": "http://s1.ticketm.net/dam/a/196/6095e742-64d1-4b15-aeac-c9733c52d196_66341_TABLET_LANDSCAPE_16_9.jpg",
                  "width": 1024,
                  "height": 576,
                  "fallback": False
                },
                 {
                  "ratio": "16_9",
                  "url": "http://s1.ticketm.net/dam/a/196/6095e742-64d1-4b15-aeac-c9733c52d196_66341_EVENT_DETAIL_PAGE_16_9.jpg",
                  "width": 205,
                  "height": 115,
                  "fallback": False
                },
                 {
                  "ratio": "3_2",
                  "url": "http://s1.ticketm.net/dam/a/196/6095e742-64d1-4b15-aeac-c9733c52d196_66341_ARTIST_PAGE_3_2.jpg",
                  "width": 305,
                  "height": 203,
                  "fallback": False
                },
                 {
                  "ratio": "16_9",
                  "url": "http://s1.ticketm.net/dam/a/196/6095e742-64d1-4b15-aeac-c9733c52d196_66341_RETINA_PORTRAIT_16_9.jpg",
                  "width": 640,
                  "height": 360,
                  "fallback": False
                },
                 {
                  "ratio": "4_3",
                  "url": "http://s1.ticketm.net/dam/a/196/6095e742-64d1-4b15-aeac-c9733c52d196_66341_CUSTOM.jpg",
                  "width": 305,
                  "height": 225,
                  "fallback": False
                },
                 {
                  "ratio": "16_9",
                  "url": "http://s1.ticketm.net/dam/a/196/6095e742-64d1-4b15-aeac-c9733c52d196_66341_RECOMENDATION_16_9.jpg",
                  "width": 100,
                  "height": 56,
                  "fallback": False
                },
                 {
                  "ratio": "3_2",
                  "url": "http://s1.ticketm.net/dam/a/196/6095e742-64d1-4b15-aeac-c9733c52d196_66341_TABLET_LANDSCAPE_3_2.jpg",
                  "width": 1024,
                  "height": 683,
                  "fallback": False
                }
              ],
              "classifications":  [
                 {
                  "primary": True,
                  "segment":  {
                    "id": "KZFzniwnSyZfZ7v7nE",
                    "name": "Sports"
                  },
                  "genre":  {
                    "id": "KnvZfZ7vAdt",
                    "name": "Golf"
                  },
                  "subGenre":  {
                    "id": "KZazBEonSMnZfZ7vFI7",
                    "name": "PGA Tour"
                  }
                }
              ],
              "_links":  {
                "self":  {
                  "href": "/discovery/v2/attractions/K8vZ917uc57?locale=en-us"
                }
              }
            }
          ]
        }
      }
    ]
  },
  "page":  {
    "size": 1,
    "totalElements": 87958,
    "totalPages": 87958,
    "number": 0
  }
}

TICKET_MASTER_EVENT_DETAILS_MOCK = {
  "_embedded": {
    "venues": [
      {
        "name": "Madison Square Garden",
        "type": "venue",
        "id": "KovZpZA7AAEA",
        "test": False,
        "url": "http://ticketmaster.com/venue/483329",
        "locale": "en-us",
        "postalCode": "10001",
        "timezone": "America/New_York",
        "city": {
          "name": "New York"
        },
        "state": {
          "name": "New York",
          "stateCode": "NY"
        },
        "country": {
          "name": "United States Of America",
          "countryCode": "US"
        },
        "address": {
          "line1": "7th Ave & 32nd Street"
        },
        "location": {
          "longitude": "-73.99160060",
          "latitude": "40.74970620"
        },
        "markets": [
          {
            "id": "35"
          },
          {
            "id": "51"
          },
          {
            "id": "55"
          },
          {
            "id": "124"
          }
        ],
        "dmas": [
          {
            "id": 200
          },
          {
            "id": 296
          },
          {
            "id": 345
          },
          {
            "id": 422
          }
        ],
        "_links": {
          "self": {
            "href": "/discovery/v2/venues/KovZpZA7AAEA?locale=en-us"
          }
        }
      }
    ],
    "attractions": [
      {
        "name": "Radiohead",
        "type": "attraction",
        "id": "K8vZ91713wV",
        "test": False,
        "url": "http://ticketmaster.com/artist/763468",
        "locale": "en-us",
        "images": [
          {
            "ratio": "16_9",
            "url": "http://s1.ticketm.net/dam/a/c4c/e751ab33-b9cd-4d24-ad4a-5ef79faa7c4c_72681_EVENT_DETAIL_PAGE_16_9.jpg",
            "width": 205,
            "height": 115,
            "fallback": False
          },
          {
            "ratio": "16_9",
            "url": "http://s1.ticketm.net/dam/a/c4c/e751ab33-b9cd-4d24-ad4a-5ef79faa7c4c_72681_RETINA_LANDSCAPE_16_9.jpg",
            "width": 1136,
            "height": 639,
            "fallback": False
          },
          {
            "ratio": "16_9",
            "url": "http://s1.ticketm.net/dam/a/c4c/e751ab33-b9cd-4d24-ad4a-5ef79faa7c4c_72681_RETINA_PORTRAIT_16_9.jpg",
            "width": 640,
            "height": 360,
            "fallback": False
          },
          {
            "ratio": "16_9",
            "url": "http://s1.ticketm.net/dam/a/c4c/e751ab33-b9cd-4d24-ad4a-5ef79faa7c4c_72681_RECOMENDATION_16_9.jpg",
            "width": 100,
            "height": 56,
            "fallback": False
          },
          {
            "ratio": "3_2",
            "url": "http://s1.ticketm.net/dam/a/c4c/e751ab33-b9cd-4d24-ad4a-5ef79faa7c4c_72681_RETINA_PORTRAIT_3_2.jpg",
            "width": 640,
            "height": 427,
            "fallback": False
          },
          {
            "ratio": "16_9",
            "url": "http://s1.ticketm.net/dam/a/c4c/e751ab33-b9cd-4d24-ad4a-5ef79faa7c4c_72681_TABLET_LANDSCAPE_16_9.jpg",
            "width": 1024,
            "height": 576,
            "fallback": False
          },
          {
            "ratio": "3_2",
            "url": "http://s1.ticketm.net/dam/a/c4c/e751ab33-b9cd-4d24-ad4a-5ef79faa7c4c_72681_ARTIST_PAGE_3_2.jpg",
            "width": 305,
            "height": 203,
            "fallback": False
          },
          {
            "ratio": "16_9",
            "url": "http://s1.ticketm.net/dam/a/c4c/e751ab33-b9cd-4d24-ad4a-5ef79faa7c4c_72681_TABLET_LANDSCAPE_LARGE_16_9.jpg",
            "width": 2048,
            "height": 1152,
            "fallback": False
          },
          {
            "ratio": "3_2",
            "url": "http://s1.ticketm.net/dam/a/c4c/e751ab33-b9cd-4d24-ad4a-5ef79faa7c4c_72681_TABLET_LANDSCAPE_3_2.jpg",
            "width": 1024,
            "height": 683,
            "fallback": False
          },
          {
            "ratio": "4_3",
            "url": "http://s1.ticketm.net/dam/a/c4c/e751ab33-b9cd-4d24-ad4a-5ef79faa7c4c_72681_CUSTOM.jpg",
            "width": 305,
            "height": 225,
            "fallback": False
          }
        ],
        "classifications": [
          {
            "primary": True,
            "segment": {
              "id": "KZFzniwnSyZfZ7v7nJ",
              "name": "Music"
            },
            "genre": {
              "id": "KnvZfZ7vAeA",
              "name": "Rock"
            },
            "subGenre": {
              "id": "KZazBEonSMnZfZ7v6dt",
              "name": "Alternative Rock"
            }
          }
        ],
        "_links": {
          "self": {
            "href": "/discovery/v2/attractions/K8vZ91713wV?locale=en-us"
          }
        }
      }
    ]
  },
  "_links": {
    "self": {
      "href": "/discovery/v2/events/G5diZfkn0B-bh?locale=en-us"
    },
    "attractions": [
      {
        "href": "/discovery/v2/attractions/K8vZ91713wV?locale=en-us"
      }
    ],
    "venues": [
      {
        "href": "/discovery/v2/venues/KovZpZA7AAEA?locale=en-us"
      }
    ]
  },
  "classifications": [
    {
      "primary": True,
      "segment": {
        "id": "KZFzniwnSyZfZ7v7nJ",
        "name": "Music"
      },
      "genre": {
        "id": "KnvZfZ7vAeA",
        "name": "Rock"
      },
      "subGenre": {
        "id": "KZazBEonSMnZfZ7v6dt",
        "name": "Alternative Rock"
      }
    }
  ],
  "dates": {
    "start": {
      "localDate": "2016-07-27",
      "localTime": "19:30:00",
      "dateTime": "2016-07-27T23:30:00Z",
      "dateTBD": False,
      "dateTBA": False,
      "timeTBA": False,
      "noSpecificTime": False
    },
    "timezone": "America/New_York",
    "status": {
      "code": "onsale"
    }
  },
  "id": "G5diZfkn0B-bh",
  "images": [
    {
      "ratio": "16_9",
      "url": "http://s1.ticketm.net/dam/a/c4c/e751ab33-b9cd-4d24-ad4a-5ef79faa7c4c_72681_EVENT_DETAIL_PAGE_16_9.jpg",
      "width": 205,
      "height": 115,
      "fallback": False
    },
    {
      "ratio": "16_9",
      "url": "http://s1.ticketm.net/dam/a/c4c/e751ab33-b9cd-4d24-ad4a-5ef79faa7c4c_72681_RETINA_LANDSCAPE_16_9.jpg",
      "width": 1136,
      "height": 639,
      "fallback": False
    },
    {
      "ratio": "16_9",
      "url": "http://s1.ticketm.net/dam/a/c4c/e751ab33-b9cd-4d24-ad4a-5ef79faa7c4c_72681_RETINA_PORTRAIT_16_9.jpg",
      "width": 640,
      "height": 360,
      "fallback": False
    },
    {
      "ratio": "16_9",
      "url": "http://s1.ticketm.net/dam/a/c4c/e751ab33-b9cd-4d24-ad4a-5ef79faa7c4c_72681_RECOMENDATION_16_9.jpg",
      "width": 100,
      "height": 56,
      "fallback": False
    },
    {
      "ratio": "3_2",
      "url": "http://s1.ticketm.net/dam/a/c4c/e751ab33-b9cd-4d24-ad4a-5ef79faa7c4c_72681_RETINA_PORTRAIT_3_2.jpg",
      "width": 640,
      "height": 427,
      "fallback": False
    },
    {
      "ratio": "16_9",
      "url": "http://s1.ticketm.net/dam/a/c4c/e751ab33-b9cd-4d24-ad4a-5ef79faa7c4c_72681_TABLET_LANDSCAPE_16_9.jpg",
      "width": 1024,
      "height": 576,
      "fallback": False
    },
    {
      "ratio": "3_2",
      "url": "http://s1.ticketm.net/dam/a/c4c/e751ab33-b9cd-4d24-ad4a-5ef79faa7c4c_72681_ARTIST_PAGE_3_2.jpg",
      "width": 305,
      "height": 203,
      "fallback": False
    },
    {
      "ratio": "16_9",
      "url": "http://s1.ticketm.net/dam/a/c4c/e751ab33-b9cd-4d24-ad4a-5ef79faa7c4c_72681_TABLET_LANDSCAPE_LARGE_16_9.jpg",
      "width": 2048,
      "height": 1152,
      "fallback": False
    },
    {
      "ratio": "3_2",
      "url": "http://s1.ticketm.net/dam/a/c4c/e751ab33-b9cd-4d24-ad4a-5ef79faa7c4c_72681_TABLET_LANDSCAPE_3_2.jpg",
      "width": 1024,
      "height": 683,
      "fallback": False
    },
    {
      "ratio": "4_3",
      "url": "http://s1.ticketm.net/dam/a/c4c/e751ab33-b9cd-4d24-ad4a-5ef79faa7c4c_72681_CUSTOM.jpg",
      "width": 305,
      "height": 225,
      "fallback": False
    }
  ],
  "locale": "en-us",
  "name": "Radiohead",
  "pleaseNote": "No tickets will be delivered prior to April 18th. Tickets are not available at the box office on the first day of the public on sale. ARRIVE EARLY: Please arrive one-hour prior to showtime. All packages, including briefcases and pocketbooks, will be inspected prior to entry.",
  "priceRanges": [
    {
      "type": "standard",
      "currency": "USD",
      "min": 80,
      "max": 80
    }
  ],
  "promoter": {
    "id": "494"
  },
  "sales": {
    "public": {
      "startDateTime": "2016-03-18T14:00:00Z",
      "startTBD": False,
      "endDateTime": "2016-07-27T21:30:00Z"
    }
  },
  "test": False,
  "type": "event",
  "url": "http://ticketmaster.com/event/3B00506AA4EA161B"
}

TICKET_MASTER_ATTRACTION_SEARCH_MOCK = {
  "_links":  {},
  "_embedded":  {
    "attractions":  [
       {
        "name": "!!!",
        "type": "attraction",
        "id": "K8vZ9175BhV",
        "test": false,
        "locale": "en-us",
        "images":  [],
        "classifications":  [
           {
            "primary": true,
            "segment":  {
              "id": "KZFzniwnSyZfZ7v7nJ",
              "name": "Music"
            },
            "genre":  {
              "id": "KnvZfZ7vAeA",
              "name": "Rock"
            },
            "subGenre":  {
              "id": "KZazBEonSMnZfZ7v6F1",
              "name": "Pop"
            }
          }
        ],
        "_links":  {
          "self":  {
            "href": "/discovery/v2/attractions/K8vZ9175BhV?locale=en-us"
          }
        }
      }
    ]
  },
  "page":  {
    "size": 1,
    "totalElements": 162165,
    "totalPages": 162165,
    "number": 0
  }
}


TICKET_MASTER_ATTRACTION_DETAILS_MOCK = {
  "name": "!!!",
  "type": "attraction",
  "id": "K8vZ9175BhV",
  "test": false,
  "locale": "en-us",
  "images":  [
     {
      "ratio": "16_9",
      "url": "http://s1.ticketm.net/dam/a/418/aa73b994-9912-4535-ba21-4865ae93a418_41291_RECOMENDATION_16_9.jpg",
      "width": 100,
      "height": 56,
      "fallback": false
    },
     {
      "ratio": "4_3",
      "url": "http://s1.ticketm.net/dam/a/418/aa73b994-9912-4535-ba21-4865ae93a418_41291_CUSTOM.jpg",
      "width": 305,
      "height": 225,
      "fallback": false
    },
     {
      "ratio": "3_2",
      "url": "http://s1.ticketm.net/dam/a/418/aa73b994-9912-4535-ba21-4865ae93a418_41291_ARTIST_PAGE_3_2.jpg",
      "width": 305,
      "height": 203,
      "fallback": false
    },
     {
      "ratio": "16_9",
      "url": "http://s1.ticketm.net/dam/a/418/aa73b994-9912-4535-ba21-4865ae93a418_41291_RETINA_PORTRAIT_16_9.jpg",
      "width": 640,
      "height": 360,
      "fallback": false
    },
     {
      "ratio": "16_9",
      "url": "http://s1.ticketm.net/dam/a/418/aa73b994-9912-4535-ba21-4865ae93a418_41291_TABLET_LANDSCAPE_LARGE_16_9.jpg",
      "width": 2048,
      "height": 1152,
      "fallback": false
    },
     {
      "ratio": "16_9",
      "url": "http://s1.ticketm.net/dam/a/418/aa73b994-9912-4535-ba21-4865ae93a418_41291_TABLET_LANDSCAPE_16_9.jpg",
      "width": 1024,
      "height": 576,
      "fallback": false
    },
     {
      "ratio": "16_9",
      "url": "http://s1.ticketm.net/dam/a/418/aa73b994-9912-4535-ba21-4865ae93a418_41291_RETINA_LANDSCAPE_16_9.jpg",
      "width": 1136,
      "height": 639,
      "fallback": false
    },
     {
      "ratio": "3_2",
      "url": "http://s1.ticketm.net/dam/a/418/aa73b994-9912-4535-ba21-4865ae93a418_41291_RETINA_PORTRAIT_3_2.jpg",
      "width": 640,
      "height": 427,
      "fallback": false
    },
     {
      "ratio": "16_9",
      "url": "http://s1.ticketm.net/dam/a/418/aa73b994-9912-4535-ba21-4865ae93a418_41291_EVENT_DETAIL_PAGE_16_9.jpg",
      "width": 205,
      "height": 115,
      "fallback": false
    },
     {
      "ratio": "3_2",
      "url": "http://s1.ticketm.net/dam/a/418/aa73b994-9912-4535-ba21-4865ae93a418_41291_TABLET_LANDSCAPE_3_2.jpg",
      "width": 1024,
      "height": 683,
      "fallback": false
    }
  ],
  "classifications":  [
     {
      "primary": true,
      "segment":  {
        "id": "KZFzniwnSyZfZ7v7nJ",
        "name": "Music"
      },
      "genre":  {
        "id": "KnvZfZ7vAeA",
        "name": "Rock"
      },
      "subGenre":  {
        "id": "KZazBEonSMnZfZ7v6F1",
        "name": "Pop"
      }
    }
  ],
  "_links":  {
    "self":  {
      "href": "/discovery/v2/attractions/K8vZ9175BhV?locale=en-us"
    }
  }
}

TICKET_MASTER_VENUE_SEARCH_MOCK = {
  "_embedded": {
    "venues": [
      {
        "_links": {
          "self": {
            "href": "/discovery/v2/venues/KovZpZAFnIEA?locale=en-us"
          }
        },
        "address": {
          "line1": "Crysler Park Marina, 13480 County Rd 2"
        },
        "city": {
          "name": "Morrisburg"
        },
        "country": {
          "name": "Canada",
          "countryCode": "CA"
        },
        "dmas": [
          {
            "id": 519
          }
        ],
        "id": "KovZpZAFnIEA",
        "locale": "en-us",
        "location": {
          "longitude": "-75.18702730",
          "latitude": "44.94535340"
        },
        "markets": [
          {
            "id": "103"
          }
        ],
        "name": "#1 Please do not use, left over from UCV initial acct set up",
        "postalCode": "K0C1X0",
        "state": {
          "name": "Ontario",
          "stateCode": "ON"
        },
        "test": false,
        "timezone": "America/Toronto",
        "type": "venue",
        "url": "http://ticketmaster.ca/venue/341396"
      },
      {
        "name": "#2 Please do not use, left over from UCV initial acct set up",
        "type": "venue",
        "id": "KovZpZAFnIJA",
        "test": false,
        "url": "http://ticketmaster.ca/venue/341395",
        "locale": "en-us",
        "postalCode": "K0C1X0",
        "timezone": "America/Toronto",
        "city": {
          "name": "Morrisburg"
        },
        "state": {
          "name": "Ontario",
          "stateCode": "ON"
        },
        "country": {
          "name": "Canada",
          "countryCode": "CA"
        },
        "address": {
          "line1": "13740 County Road 2"
        },
        "location": {
          "longitude": "-75.18635300",
          "latitude": "44.89937100"
        },
        "markets": [
          {
            "id": "103"
          }
        ],
        "dmas": [
          {
            "id": 519
          }
        ],
        "_links": {
          "self": {
            "href": "/discovery/v2/venues/KovZpZAFnIJA?locale=en-us"
          }
        }
      }
    ]
  },
  "_links": {
    "self": {
      "href": "/discovery/v2/venues.json?view=null&keyword=UCV{&page,size,sort}",
      "templated": true
    }
  },
  "page": {
    "size": 20,
    "totalElements": 2,
    "totalPages": 1,
    "number": 0
  }
}


TICKET_MASTER_VENUE_DETAILS_MOCK = {
  "name": "#1 Please do not use, left over from UCV initial acct set up",
  "type": "venue",
  "id": "KovZpZAFnIEA",
  "test": false,
  "locale": "en-us",
  "postalCode": "K0C1X0",
  "timezone": "America/Toronto",
  "city":  {
    "name": "Morrisburg"
  },
  "state":  {
    "name": "Ontario",
    "stateCode": "ON"
  },
  "country":  {
    "name": "Canada",
    "countryCode": "CA"
  },
  "address":  {
    "line1": "Crysler Park Marina, 13480 County Rd 2"
  },
  "location":  {
    "longitude": "-75.18702730",
    "latitude": "44.94535340"
  },
  "markets":  [
     {
      "id": "103"
    }
  ],
  "_links":  {
    "self":  {
      "href": "/discovery/v2/venues/KovZpZAFnIEA?locale=en-us"
    }
  }
}
