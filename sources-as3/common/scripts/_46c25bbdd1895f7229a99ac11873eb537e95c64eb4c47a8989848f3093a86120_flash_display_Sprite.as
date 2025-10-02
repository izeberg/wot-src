package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _46c25bbdd1895f7229a99ac11873eb537e95c64eb4c47a8989848f3093a86120_flash_display_Sprite extends Sprite
   {
       
      
      public function _46c25bbdd1895f7229a99ac11873eb537e95c64eb4c47a8989848f3093a86120_flash_display_Sprite()
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
