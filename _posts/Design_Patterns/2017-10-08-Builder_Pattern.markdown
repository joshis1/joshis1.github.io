---
layout: post
title:  "The Builder Pattern in C++"
date:   2017-10-08 10:13:31 +1300
categories: Design_Patterns
description: A C++ example of assembling tuner configurations with builders and an optional director.
---

The Builder pattern separates the construction of a complex object from its representation. This article uses tuner configurations to illustrate a classic builder and director arrangement.

**What is a builder pattern?**

It is a pattern to construct a complex object, which is made of a simple
objects. Here, the recipe to make the complex object is only known to the
director. The builder knows the specifics to create the complex object, and it
is hidden from the client. The director calls the builder to build the
specifics.

**When is the ‘Builder Pattern’ required?**

It is required to create a number of objects, whose process of creation is
same. However, they differ in the representation. Basically, the construction
process/protocol is common, but the content is different. Here, the object is
build step by step with the aid of the director.

**How a ‘Builder Pattern’ is designed?**

1. Firstly, set a plan of the object that has the set of common behavioural
attributes. This is a sort of ‘Strategy/Behavioural Pattern’.
2. Create the concrete class from the strategy/behavioural interface class –
point number 1.
3. Make an abstract builder, which will set the attributes of the object.
4. Extend the abstract builder to create a concrete builder class. This should
set the attributes according to the desired concrete class.
5. Create a direct or class that will have the builder interface. The director
class should have the recipe to make the desired product using the builder
reference. The direct or class should also return the final product to the client .
6. It is a composition type where the ‘builder’ has the ‘object ’ – composition.
Also, the director has the builder reference – aggregation ( builder object –
specs is passed by the client ).

**Analogy:**

The director is like a waiter in the restaurant. The builders are the restaurant
staff . A client will speak to director/waiter to order a product. Before
ordering to the director, a client will get a specific(menu) from the builder.
Also, a client will pass this specific to the waiter/director.
Later, a direct or/waiter will prepare (build) the order and will pass to the
client. In order to build the customer order, the waiter needs to interact with
the builder. It will instruct the builder on what needs to be set.

**Problem/scenario:** In a Set -top box, we have a different types of tuners.
For example, terrestrial and satellite. All these tuners have the same
behaviours like – FEC, Polarisation, and modulation. However, the attributes
of these behaviours are different. Design a pattern to construct these objects.

**Analysis -** The terrestrial and satellite objects are having the similar
kind of construction. However, they are represented differently. Here, we can
use a builder pattern to create these two objects.

Let’s see the UML diagram here.

<img src="/assets/img/Builder_Pattern_UML.png" alt="Builder_Pattern_UML">

1. The object interface is tuner here. The tuner has the following properties.

  a. setTunerFEC() <br>
  b. setTunerPolarization() <br>
  c. setTunerModulationType() <br>
    This is nothing but a behaviour of the object – tuner.

2. Create a builder abstract class.
  a. This should build the TunerFEC(), by calling the tuner behaviour methods –
      setTunerFEC()
  b. This should build the TunerPolarization(), by calling the tuner behaviour
      methods – set TunerPolarization()
  c. This should build the TunerModulationType(), by calling the tuner behaviour
      methods – setTunerModulationType()
3. Create a concrete builder class – tunerTerrestrialBuilder()
4. Create a concrete builder class – tunerSatelliteBuilder()
5. Create a director/Engineer class that will build the final product. This will
   hold the reference to the builder. With the aid of a builder reference, it will
   call the specific build. For example, build TunerFEC, build
   TunerPolarization(), and build setTunerModulationType().

6. Finally, the director will return the final product.

7. A client will create a builder type. For example, terrestrial type.
  Later, it will pass the terrestrial builder object to the director. The director
  will call the build operations of the terrestrial builder to create a final product.
  Interface or plan of the tuner object.

{% highlight cpp %}

  class Ituner
  {
  public:
    virtual void setTunerFEC(float fec) = 0;
    virtual void setTunerPolarization(std::string polar) = 0;
    virtual void setTunerModulationType(std::string mod) = 0;
    virtual ~Ituner();
  };

  Ituner::~Ituner()
  {
    std::cout<<"Ituner destructor called"<<std::endl;
  }
    Concrete Tuner object to set the behaviour. A sort of strategy pattern.
    class tuner: public Ituner
    {
      private:
        float m_fec;
        std::string m_polar;
        std::string m_mod;
      public:
          tuner(): m_fec(0),m_polar("NONE"),m_mod("NONE")
          {
            std::cout<<"Tuner Initialized"<<std::endl;
          }
          void setTunerFEC(float fec)
          {
            m_fec = fec;
          }
          float getTunerFEC(void)
          {
            return m_fec;
          }
          void setTunerPolarization(std::string polar)
          {
            m_polar = polar;
          }
          std::string getTunerPolarization(void)
          {
            return m_polar;
          }
          void setTunerModulationType(std::string mod)
          {
            m_mod = mod;
          }
          std::string getTunerModulationType(void)
          {
            return m_mod;
          }
  };

  {% endhighlight %}

  Here is the abstract builder class.

  {% highlight cpp %}

  class ITunerBuilder
  {
    public:
      virtual void buildTunerFEC() = 0;
      virtual void buildTunerPolarization() = 0;
      virtual void buildTunerModulationType() = 0;
      virtual tuner getTuner() = 0;
      virtual ~ITunerBuilder() = 0;
    protected:
      tuner m_tuner;
  };

  ITunerBuilder::~ITunerBuilder()
  {
    std::cout<<"Virtual destructor of ItunerBuilder"<<std::endl;
  }

  {% endhighlight %}

  Here is the concrete tuner builder – terrestrial type.

  {% highlight cpp %}

  class tunerTerrestrialBuilder: public ITunerBuilder
  {
    public:
      tunerTerrestrialBuilder()
      {
      }
      ~tunerTerrestrialBuilder()
      {
        std::cout<<"Tuner terrestrial Builder deleted"<<std::endl;
      }
      void buildTunerFEC()
      {
        m_tuner.setTunerFEC(0.8);
      }
      void buildTunerPolarization()
      {
        m_tuner.setTunerPolarization("Vertical");
      }
      void buildTunerModulationType()
      {
        m_tuner.setTunerModulationType("QPSK");
      }
      tuner getTuner()
      {
        return m_tuner;
      }
  };

{% endhighlight %}

Here is the concrete tuner builder – satellite type.

{% highlight cpp %}
class tunerSatelliteBuilder: public ITunerBuilder
{
  public:
    tunerSatelliteBuilder()
    {
    }
    ~tunerSatelliteBuilder()
    {
      std::cout<<"Tuner terrestrial Builder deleted"<<std::endl;
    }
    void buildTunerFEC()
    {
      m_tuner.setTunerFEC(0.75);
    }
    void buildTunerPolarization()
    {
      m_tuner.setTunerPolarization("Horizontal");
    }
    void buildTunerModulationType()
    {
      m_tuner.setTunerModulationType("QPSK2");
    }
    tuner getTuner()
    {
      return m_tuner;
    }
};

{% endhighlight %}

Let’s make a director/Engineer to take up the order of a client.

{% highlight cpp %}

class tunerEngineer
{
  private:
    ITunerBuilder * p_tunerBuilder;
    /** forced to use the parameter constructor only ** /
    tunerEngineer();
    public:
        tunerEngineer(ITunerBuilder * tunerBuilder)
        {
          p_tunerBuilder = tunerBuilder;
        }
        tuner getTuner()
        {
          return (p_tunerBuilder->getTuner());
        }
        void makeTuner()
        {
          p_tunerBuilder->buildTunerFEC();
          p_tunerBuilder->buildTunerModulationType();
          p_tunerBuilder->buildTunerPolarization();
        }
};

{% endhighlight %}

Now, the main file for a client to test the builder pattern.

{% highlight cpp %}

int main(void)
{
  tuner terrestrialTuner;
  /** this is a spec or a blue print that needs to be passed to the engineer/director**/
  ITunerBuilder * pTerrBuilder = new tunerTerrestrialBuilder();
  tunerEngineer * pTunerDirector = new tunerEngineer(pTerrBuilder);
  pTunerDirector->makeTuner();
  terrestrialTuner = pTunerDirector->getTuner();
  std::cout<<"Terrestrial FEC TYPE is "<<terrestrialTuner.getTunerFEC()<<std::endl;
  delete pTunerDirector;
  delete pTerrBuilder;
  tuner satelliteTuner;
  ITunerBuilder * pSatBuilder = new tunerSatelliteBuilder();
  pTunerDirector = new tunerEngineer(pSatBuilder);
  pTunerDirector->makeTuner();
  satelliteTuner = pTunerDirector->getTuner();
  std::cout<<"Terrestrial FEC TYPE is "<<satelliteTuner.getTunerFEC()<<std::endl;
  delete pTunerDirector;
  delete pSatBuilder;
  return 0;
}

{% endhighlight %}

**Difference between Builder and Factory Pattern.**
<br>
The factory pattern creates the product in one step. However, the builder
pattern creates the product in multiple steps. The builder pattern uses
composition internally. It is a combination of strategy/behavioural
pattern. Here, the builder object ‘has a’ tuner object.

You can download the entire code here.

[Source_code_BuilderPattern](https://drive.google.com/open?id=1ncwbzoSmpxX9x-tOjzeVTJ6iEqGbUtFT)
