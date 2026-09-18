package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _44f60e5271d8ee2ffdfb705fe45fb0464ace2f1bb65974f5eaa09c105c982635_flash_display_Sprite extends Sprite
   {
       
      
      public function _44f60e5271d8ee2ffdfb705fe45fb0464ace2f1bb65974f5eaa09c105c982635_flash_display_Sprite()
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
