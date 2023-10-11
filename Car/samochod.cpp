#include <iostream>

//Numerki przy "zmiana_bieg", "przys_zwol" mowia ktory trzeba przycisk wcisnac
//Odpowiada za biegi
int biegi_int(int bieg,int predkosc, int zmien_bieg)
{
    if(zmien_bieg==3)
    {
        bieg+=1;
    }
    
    else if(zmien_bieg==4)
    {
        bieg-=1;
    }
    return bieg;
}

//Odpowiada za przyspieszanie i hamowanie
int predkosc_int(int predkosc,int bieg,int obroty, int przys_zwol)
{
    if(przys_zwol==1)
    {
        //Jak probojesz przyspieszyc na biegu neutralnym
        if(bieg==0)
        {
            std::cout<<"\n!!Bieg neutralny!!\n\n";
        }
        //Dla reszty (przyspieszenie)
        else
        {
            predkosc+=5;
        }
    }
    else if(przys_zwol==2)
    {
        //Jak probojesz zwolnic na biegu neutralnym
        if(bieg==0)
        {
            std::cout<<"\n!!Bieg neutralny!!\n\n";
        }
        
        //Dla reszty (hamowanie)
        else
        {
            predkosc-=5;
        }
    }
    return predkosc;
}

//Odpowiada za obroty
int obroty_int(int obroty, int bieg, int predkosc)
{
    if(bieg==0)
    {
        obroty=0;
    }
    else if(bieg==1)
    {
        if(predkosc==5)
        {
            obroty=850;
        }
        else
        {
            obroty=predkosc/5*500;
        }
    }
    else if(bieg==2)
    {
        obroty=predkosc/5*315;
    }
    else if(bieg==3)
    {
        obroty=predkosc/5*210;
    }
    else if(bieg==4)
    {
        obroty=predkosc/5*165;
    }
    else if(bieg==5)
    {
        obroty=predkosc/5*125;
    }
    else if(bieg=6)
    {
        obroty=predkosc/5*100;
    }
    return obroty;
}

//odpowiada za dzialanie ogolne
int samochod()
{
    int predkosc,bieg, obroty,x,wybor;
    predkosc=0;
    bieg=0;
    obroty=0;
    x=1;
    while(x==1)
    {
        //Wybor co uzytkownik chce zrobic
        if (bieg==0)
        {
            std::cout<<"Predkosc: "<<predkosc<<" km/h"<<std::endl<<"Bieg: "<<"N"<<std::endl<<"Obroty: "<<obroty<<std::endl<<std::endl;
        }
        else
        {
            std::cout<<"Predkosc: "<<predkosc<<" km/h"<<std::endl<<"Bieg: "<<bieg<<std::endl<<"Obroty: "<<obroty<<std::endl<<std::endl;
        }
        std::cout<<"1.Przyspiesz\n2.Zwolnij\n3.Zwieksz bieg\n4.Zmniejsz bieg\n5.Zakoncz program\n";
        std::cin>>wybor;
        system("cls");

        switch(wybor)
        {
        //Przyspieszanie
        case 1:
        if((predkosc>0 && bieg>=1) || (predkosc>=0 && bieg==1))
        {
            predkosc=predkosc_int(predkosc,bieg,obroty, wybor);
            obroty=obroty_int(obroty, bieg, predkosc);
        }
        else if(predkosc==0 && bieg>1)
        {
            std::cout<<"\n!!Za wysoki bieg!!\n\n";
        }
        else if(bieg==0)
        {
            std::cout<<"\n!!Bieg neutralny!!\n\n";
        }
        break;
        
        //Hamowanie
        case 2:
        if(predkosc>0)
        {
            predkosc=predkosc_int(predkosc, bieg, obroty, wybor);
            obroty=obroty_int(obroty, bieg, predkosc);
        }
        else
        {
            std::cout<<"\n!!Nie ruszyles!!\n\n";
        }
        break;
        //Bieg wyzszy
        
        case 3:
        if(bieg>=0 && bieg<6)
        {
            if(bieg==0 || (bieg>0 && predkosc==0))
            {
                bieg=biegi_int(bieg,predkosc, wybor);
                obroty=obroty_int(obroty, bieg, predkosc);
            }
            else if(predkosc>=5)
            {
                bieg=biegi_int(bieg,predkosc, wybor);
                obroty=obroty_int(obroty, bieg, predkosc);
            }
        }
        else
        {
            std::cout<<"\n!!Brak wyzszego biegu!!\n\n";
        }
        break;
        
        //Bieg nizszy
        case 4:
        if(bieg>=1)
        {
            bieg=biegi_int(bieg,predkosc, wybor);
            obroty=obroty_int(obroty, bieg, predkosc);
        }
        else
        {
            std::cout<<"\n!!Brak nizszego biegu!!\n\n";
        }
        break;
        
        //Wylacz samochod
        case 5:
        predkosc=0;
        bieg=0;
        obroty=0;
        x=0;
        break;
        }
        
        
        //Dla najwyzszego biegu
        if(bieg==6)
        {
            if(obroty>=3200 && obroty<3500)
            {
                std::cout<<"\n!!Zwolnij!!\n\n";
            }
            else if(obroty>=3500)
            {
                std::cout<<"\n!!BUM!!\n\n";
                x=0;
            }
            else if(obroty<=1500 && predkosc>0)
            {
                std::cout<<"\n!!Samochod zgasl!!\n\n";
                x=0;
            }
            else if(obroty<=1800 && predkosc>0)
            {
                std::cout<<"\n!!Zmien bieg na nizszy!!\n\n";
            }
        }
        else if(bieg>1 && obroty<=850 && predkosc>0)
        {
            std::cout<<"\n!!Samochod zgasl!!\n\n";
            x=0;
        }
        else if(bieg>0 && bieg<6)
        {
            if(obroty>=3500)
            {
                std::cout<<"\n!!BUM!!\n\n";
                x=0;
            }
            else if(obroty>=2500)
            {
                std::cout<<"\n!!Zmien bieg na wyzszy!!\n\n";
            }
            else if(obroty<=1500 && bieg!=1 && predkosc>0)
            {
                std::cout<<"\n!!Zmien bieg na nizszy!!\n\n";
            }
        }
    }
    return 0;
}


int main()
{
    //Wybor start/stop
    int on_off,x;
    std::cout<<"1.Uruchom samochod   2.Wyjdz z programu\n";
    std::cin>>on_off;
    std::cout<<std::endl<<std::endl<<std::endl;
    switch(on_off)
    {
    case 1:
    x=samochod();
    break;
    default:
    break;
    }
}
