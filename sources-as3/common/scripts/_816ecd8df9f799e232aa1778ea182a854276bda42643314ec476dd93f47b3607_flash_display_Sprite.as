package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _816ecd8df9f799e232aa1778ea182a854276bda42643314ec476dd93f47b3607_flash_display_Sprite extends Sprite
   {
       
      
      public function _816ecd8df9f799e232aa1778ea182a854276bda42643314ec476dd93f47b3607_flash_display_Sprite()
      {
         super();
      }
      
      public function allowDomainInRSL(... rest) : void
      {
         Security.allowDomain.apply(null,rest);
      }
      
      public function allowInsecureDomainInRSL(... rest) : void
      {
         Security.allowInsecureDomain.apply(null,rest);
      }
   }
}
